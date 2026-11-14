"""Chạy agent thật trên một split và lưu trace + metric tự động + file nhãn để chấm tay.

    python -m src.run_agent --split dev --tag baseline --method dense --top-k 3 --budget 6000 --max-searches 3
    python -m src.run_agent --split dev --tag smoke --limit 2

Đầu ra results/agent/<split>/<tag>/:
  traces.json        trace đầy đủ từng câu (tool call, kết quả, context, câu trả lời, citation, token, chi phí, lỗi)
  summary.json       metric tự động: status, tool use, phân bố số lượt search, Context Evidence Rate, token, chi phí
  review.json        nhãn cần NGƯỜI chấm (answer_grade, citation_support, abstention_correct) — để null
  review_sheet.md    bảng đọc nhanh: câu hỏi, đáp án chuẩn, câu trả lời agent, đoạn được trích
Gold chỉ dùng sau khi agent trả lời, để tính hint tự động; không vào prompt hay retrieval.
"""
from __future__ import annotations

import argparse
import json
import statistics
import time
from collections import Counter

import anthropic

from src import config
from src.agent import Agent, AgentConfig
from src.evidence import chunk_hits
from src.retrieval import build, load_chunks

QUESTIONS = config.ROOT / "data" / "benchmark" / "questions.json"
RESULTS = config.ROOT / "results" / "agent"


def frac(n, d):
    return {"n": n, "N": d, "rate": round(n / d, 4) if d else None}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", required=True, choices=("dev", "test"))
    ap.add_argument("--tag", required=True)
    ap.add_argument("--method", default="dense")
    ap.add_argument("--top-k", type=int, default=3)
    ap.add_argument("--budget", type=int, default=6000, help="tổng ký tự context cho cả lượt chạy")
    ap.add_argument("--max-searches", type=int, default=3)
    ap.add_argument("--neighbors", action="store_true", help="thêm chunk liền kề cùng Điều")
    ap.add_argument("--prompt", default="v1", choices=("v1", "v2_precise"))
    ap.add_argument("--effort", default=config.LLM_EFFORT)
    ap.add_argument("--model", default=config.LLM_MODEL)
    ap.add_argument("--limit", type=int, default=0, help="chỉ chạy N câu đầu (smoke test)")
    ap.add_argument("--ids", nargs="*", help="chỉ chạy các ID này")
    args = ap.parse_args()

    qs = [q for q in json.loads(QUESTIONS.read_text(encoding="utf-8")) if q["split"] == args.split]
    if args.ids:
        qs = [q for q in qs if q["id"] in set(args.ids)]
    if args.limit:
        qs = qs[: args.limit]
    chunks = load_chunks()
    retriever = build([args.method], chunks)[args.method]
    cfg = AgentConfig(name=args.tag, method=args.method, top_k=args.top_k, budget_chars=args.budget,
                      max_searches=args.max_searches, neighbors=args.neighbors, prompt=args.prompt,
                      effort=args.effort, model=args.model)
    agent = Agent(retriever, cfg, chunks)

    traces = []
    for i, q in enumerate(qs, 1):
        t0 = time.perf_counter()
        try:
            out = agent.run(q["question"], q.get("filter"))  # chỉ câu hỏi + filter người dùng
        except (anthropic.APIError, Exception) as e:  # ghi lỗi thật, không thay bằng kết quả giả
            out = {"status": "error", "answer": "", "citations": [], "events": [{"event": "error", "type": type(e).__name__,
                   "message": str(e)[:500]}], "context_ids": [], "n_searches": 0, "usage": {"cost_usd": 0.0, "input": 0, "output": 0},
                   "elapsed_s": round(time.perf_counter() - t0, 2), "config": cfg.__dict__}
        tr = {"query_id": q["id"], "split": q["split"], "type": q["type"], "answerable": q["answerable"],
              "question": q["question"], "filter": q.get("filter"), "model": cfg.model, **out}
        if q["answerable"]:  # chấm tự động SAU khi chạy
            by_id = {c["id"]: c for c in chunks}
            tr["auto"] = {
                "context_has_evidence": any(chunk_hits(by_id[c], q["gold"]) for c in out.get("context_ids", [])),
                "cited_has_evidence": any(chunk_hits(by_id[c], q["gold"]) for c in out.get("citations", [])),
                "first_search_hit3": bool(out.get("events")) and out["events"][0].get("event") == "search" and
                                     any(chunk_hits(by_id[r["id"]], q["gold"]) for r in out["events"][0]["results"][:3])}
        traces.append(tr)
        print(f"[{i}/{len(qs)}] {q['id']} {tr['status']:8} searches={tr.get('n_searches')} "
              f"{tr.get('elapsed_s')}s ${tr['usage'].get('cost_usd', 0):.5f} {tr.get('stop_reason', '')}", flush=True)

    ok = [t for t in traces if t["status"] != "error"]
    ans = [t for t in ok if t["answerable"]]
    una = [t for t in ok if not t["answerable"]]
    n_cit = sum(len(t["citations"]) for t in ok)
    summary = {
        "tag": args.tag, "split": args.split, "config": cfg.__dict__, "n": len(traces),
        "status": dict(Counter(t["status"] for t in traces)),
        "errors": [{"id": t["query_id"], "events": t["events"]} for t in traces if t["status"] == "error"],
        "tool_use": frac(sum(t["n_searches"] > 0 for t in ok), len(ok)),
        "searches_distribution": dict(sorted(Counter(t["n_searches"] for t in ok).items())),
        "stop_reasons": dict(Counter(t.get("stop_reason") for t in traces)),
        "answerable": {
            "context_evidence_rate": frac(sum(t["auto"]["context_has_evidence"] for t in ans), len(ans)),
            "first_search_evidence_hit3": frac(sum(t["auto"]["first_search_hit3"] for t in ans), len(ans)),
            "answered": frac(sum(t["status"] == "answered" for t in ans), len(ans)),
            "false_abstention": frac(sum(t["status"] == "abstain" for t in ans), len(ans)),
            "answered_with_cited_evidence_auto": frac(sum(t["auto"]["cited_has_evidence"] for t in ans), len(ans)),
        },
        "unanswerable": {"abstained": frac(sum(t["status"] == "abstain" for t in una), len(una))},
        "citations": {"total": n_cit, "in_context": sum(c in t["context_ids"] for t in ok for c in t["citations"]),
                      "answers_with_citation": frac(sum(bool(t["citations"]) for t in ok if t["status"] == "answered"),
                                                    sum(t["status"] == "answered" for t in ok))},
        "tokens": {"input": sum(t["usage"].get("input", 0) for t in traces), "output": sum(t["usage"].get("output", 0) for t in traces)},
        "cost_usd": round(sum(t["usage"].get("cost_usd", 0) for t in traces), 6),
        "latency_s": {"median": statistics.median(t["elapsed_s"] for t in traces), "max": max(t["elapsed_s"] for t in traces)},
        "note": "Grounded answer, citation support và abstention đúng phải do người chấm trong review.json; "
                "các trường *_auto chỉ là gợi ý dựa trên gold sau khi chạy.",
    }

    qmap = {q["id"]: q for q in qs}
    review = [{"query_id": t["query_id"], "answerable": t["answerable"], "status": t["status"],
               "answer_grade": None if t["answerable"] else None,
               "citation_support": [None] * len(t["citations"]),
               **({} if t["answerable"] else {"abstention_correct": None}), "reason": ""}
              for t in traces if t["status"] != "error"]
    lines = [f"# Review sheet — {args.split} / {args.tag}", "",
             f"Model {cfg.model}, method {cfg.method}, top-k {cfg.top_k}, budget {cfg.budget_chars} ký tự, "
             f"max_searches {cfg.max_searches}, neighbors {cfg.neighbors}, prompt {cfg.prompt}, effort {cfg.effort}.", ""]
    for t in traces:
        q = qmap[t["query_id"]]
        lines += [f"## {t['query_id']} · {q['type']} · {'có đáp án' if q['answerable'] else 'THIẾU BẰNG CHỨNG'} · status `{t['status']}`",
                  f"**Hỏi:** {q['question']}", ""]
        lines += [f"**Đáp án chuẩn:** {q['expected_answer']}", f"**Gold:** {q['gold']}", ""] if q["answerable"] else \
                 [f"**Lý do thiếu:** {q['absence_reason']}", ""]
        for e in t["events"]:
            if e.get("event") == "search":
                lines.append(f"- search `{e['query']}` → mới: {', '.join(x['alias'] for x in e['new_context']) or '—'}")
        lines += ["", f"**Agent:** {t['answer']}", ""]
        for cid in t["citations"]:
            c = next(x for x in chunks if x["id"] == cid)
            lines += [f"> `{cid}` (trang {c['metadata'].get('pages')}): {c['text'][:600]}", ""]
        if t["answerable"]:
            lines.append(f"_auto: context có evidence = {t['auto']['context_has_evidence']}, "
                         f"citation chứa evidence = {t['auto']['cited_has_evidence']}_")
        lines += ["", "---", ""]

    out = RESULTS / args.split / args.tag
    out.mkdir(parents=True, exist_ok=True)
    for name, obj in (("traces.json", traces), ("summary.json", summary)):
        (out / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")
    rv = out / "review.json"
    if rv.exists():  # không ghi đè nhãn người đã chấm
        rv = out / "review.template.json"
    rv.write_text(json.dumps(review, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out / "review_sheet.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("status", "tool_use", "searches_distribution", "answerable",
                                              "unanswerable", "citations", "tokens", "cost_usd", "latency_s")},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
