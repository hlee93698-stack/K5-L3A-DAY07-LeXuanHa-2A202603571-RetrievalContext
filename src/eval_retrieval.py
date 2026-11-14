"""Benchmark retrieval + context (không gọi LLM) trên một split.

    python -m src.eval_retrieval --split dev
    python -m src.eval_retrieval --split dev --methods dense bm25 --top-k 3 --budget 3000 --tag mytry

Metric (mẫu số = số câu có đáp án của split; câu thiếu bằng chứng chỉ được ghi trace):
  Hit@1, Evidence Hit@3      evidence hợp lệ ở top-1 / top-3 (định nghĩa hit: src/evidence.py)
  MRR@10, Hit@10             để thấy evidence có nằm sâu hơn top-3 không
  Context Evidence Rate      evidence hợp lệ nằm trong context cuối (top-k đóng gói theo budget ký tự)
Gold chỉ dùng để chấm SAU khi retrieval trả kết quả. Không chạy --split test trước khi chốt cấu hình.
"""
from __future__ import annotations

import argparse
import json
import statistics
import time
from pathlib import Path

from src import config
from src.context import pack_context
from src.evidence import chunk_hits
from src.retrieval import build, load_chunks

QUESTIONS = config.ROOT / "data" / "benchmark" / "questions.json"
RESULTS = config.ROOT / "results" / "retrieval"
DEFAULT_METHODS = ["dense", "bm25", "bm25_ngram2", "hybrid_rrf"]
DEEP_K = 10


def frac(n: int, d: int) -> dict:
    return {"n": n, "N": d, "rate": round(n / d, 4) if d else None}


def run_method(retriever, questions, *, top_k: int, budget: int, use_filter: bool) -> tuple[list, dict]:
    traces = []
    for q in questions:
        flt = q.get("filter") if use_filter else None
        t0 = time.perf_counter()
        deep = retriever.search(q["question"], filters=flt, top_k=max(DEEP_K, top_k))
        ms = (time.perf_counter() - t0) * 1000
        ctx = pack_context(deep[:top_k], budget)
        tr = {"query_id": q["id"], "split": q["split"], "type": q["type"], "answerable": q["answerable"],
              "question": q["question"], "query": q["question"], "query_rewritten": None,
              "filter": flt, "method": retriever.name, "top_k": top_k, "elapsed_ms": round(ms, 1),
              "results": [{"rank": r["rank"], "id": r["id"], "source_id": r["source_id"], "page": r["page"],
                           "page_end": r["metadata"].get("page_end"), "score": round(r["score"], 6),
                           **({"components": r["components"]} if "components" in r else {}),
                           "text_preview": r["text"][:160]} for r in deep],
              **ctx}
        if q["answerable"]:
            flags = [chunk_hits(r, q["gold"]) for r in deep]
            first = flags.index(True) + 1 if any(flags) else None
            tr.update({"hit_at_rank": flags, "first_hit_rank": first, "hit1": bool(flags[:1] and flags[0]),
                       "hit3": any(flags[:3]), "hit10": any(flags[:DEEP_K]),
                       "context_hit": any(f and r["id"] in ctx["context_ids"] for f, r in zip(flags, deep))})
        traces.append(tr)

    ans = [t for t in traces if t["answerable"]]
    summary = {
        "method": retriever.name, "split": questions[0]["split"], "top_k": top_k, "budget_chars": budget,
        "use_filter": use_filter, "n_answerable": len(ans), "n_unanswerable": len(traces) - len(ans),
        "hit1": frac(sum(t["hit1"] for t in ans), len(ans)),
        "evidence_hit3": frac(sum(t["hit3"] for t in ans), len(ans)),
        "hit10": frac(sum(t["hit10"] for t in ans), len(ans)),
        "mrr10": round(statistics.mean(1 / t["first_hit_rank"] if t["first_hit_rank"] else 0 for t in ans), 4),
        "context_evidence_rate": frac(sum(t["context_hit"] for t in ans), len(ans)),
        "avg_context_chars": round(statistics.mean(t["context_chars"] for t in traces), 1),
        "dropped_by_budget": sum(len(t["dropped_ids"]) for t in traces),
        "median_ms": round(statistics.median(t["elapsed_ms"] for t in traces), 1),
        "p90_ms": round(sorted(t["elapsed_ms"] for t in traces)[int(0.9 * (len(traces) - 1))], 1),
        "cost_usd": 0.0,
        "misses_at3": [t["query_id"] for t in ans if not t["hit3"]],
        "misses_at1": [t["query_id"] for t in ans if not t["hit1"]],
    }
    return traces, summary


def table(summaries: list[dict]) -> str:
    def f(x):
        return f"{x['n']}/{x['N']} ({x['rate']:.0%})"
    rows = ["| Phương pháp | Filter | top-k | Budget (ký tự) | Hit@1 | Evidence Hit@3 | Hit@10 | MRR@10 | Context Evidence Rate | Median / p90 ms | Chi phí | Miss@3 |",
            "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for s in summaries:
        rows.append(f"| {s['method']} | {'có' if s['use_filter'] else 'không'} | {s['top_k']} | {s['budget_chars']} | "
                    f"{f(s['hit1'])} | {f(s['evidence_hit3'])} | {f(s['hit10'])} | {s['mrr10']:.3f} | "
                    f"{f(s['context_evidence_rate'])} | {s['median_ms']} / {s['p90_ms']} | $0 | "
                    f"{', '.join(s['misses_at3']) or '—'} |")
    return "\n".join(rows)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", required=True, choices=("dev", "test"))
    ap.add_argument("--methods", nargs="+", default=DEFAULT_METHODS)
    ap.add_argument("--top-k", type=int, default=3)
    ap.add_argument("--budget", type=int, default=3000, help="context budget, đơn vị ký tự")
    ap.add_argument("--no-filter", action="store_true", help="bỏ filter người dùng cung cấp")
    ap.add_argument("--tag", default="", help="hậu tố thư mục kết quả cho cấu hình thử nghiệm")
    args = ap.parse_args()

    questions = [q for q in json.loads(QUESTIONS.read_text(encoding="utf-8")) if q["split"] == args.split]
    chunks = load_chunks()
    t0 = time.perf_counter()
    retrievers = build(args.methods, chunks)
    setup_s = time.perf_counter() - t0

    out_root = RESULTS / args.split / (args.tag or "methods")
    summaries = []
    for name, ret in retrievers.items():
        traces, summary = run_method(ret, questions, top_k=args.top_k, budget=args.budget,
                                     use_filter=not args.no_filter)
        summary["setup_seconds_all_methods"] = round(setup_s, 2)
        d = out_root / name
        d.mkdir(parents=True, exist_ok=True)
        (d / "traces.json").write_text(json.dumps(traces, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (d / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        summaries.append(summary)

    md = (f"# Retrieval {args.split} — {args.tag or 'methods'}\n\n"
          f"Corpus: {len(chunks)} chunk ({config.DAY6_COLLECTION}), embedding {config.EMBEDDING_MODEL}. "
          f"Câu có đáp án: {summaries[0]['n_answerable']}; câu thiếu bằng chứng (không vào mẫu số): "
          f"{summaries[0]['n_unanswerable']}. Setup (load model + index): {setup_s:.1f}s.\n\n{table(summaries)}\n")
    (out_root / "comparison.md").write_text(md, encoding="utf-8")
    (out_root / "comparison.json").write_text(json.dumps(summaries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(md)


if __name__ == "__main__":
    main()
