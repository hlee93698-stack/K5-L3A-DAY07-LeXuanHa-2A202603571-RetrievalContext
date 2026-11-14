"""So sánh các cấu hình agent trên một split -> results/agent/<split>/comparison.md (+ .json).

    python -m src.compare_agent --split dev

Gồm: metric retrieval với query gốc (từ src.eval_retrieval), metric agent tự động, và — nếu
review.json của cấu hình đã chấm đủ — Grounded answer / citation hợp lệ / abstention qua
starter/agent_metrics.aggregate. Bảng từng câu cho thấy chỗ các cấu hình khác nhau.
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys

from src import config

sys.path.insert(0, str(config.ROOT / "starter"))
from agent_metrics import aggregate  # noqa: E402

AGENT = config.ROOT / "results" / "agent"
RETR = config.ROOT / "results" / "retrieval"
CASES = config.ROOT / "data" / "benchmark" / "cases.json"


def f(x):
    return f"{x['n']}/{x['N']}" if x and x.get("N") else "—"


def load(p):
    return json.loads(p.read_text(encoding="utf-8"))


def reviewed(review) -> bool:
    for r in review:
        if any(v is None for v in r.get("citation_support", [])):
            return False
        if r["answerable"] and r.get("answer_grade") is None:
            return False
        if not r["answerable"] and r.get("abstention_correct") is None:
            return False
    return bool(review)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", required=True, choices=("dev", "test"))
    ap.add_argument("--tags", nargs="*")
    args = ap.parse_args()
    root = AGENT / args.split
    tags = args.tags or sorted(p.parent.name for p in root.glob("*/summary.json"))
    cases = [c for c in load(CASES) if c["split"] == args.split]

    rows, per_q, out = [], {}, []
    for tag in tags:
        s, traces = load(root / tag / "summary.json"), load(root / tag / "traces.json")
        cfg = s["config"]
        retr_p = RETR / args.split / "methods" / cfg["method"] / "summary.json"
        retr = load(retr_p) if retr_p.exists() else {}
        correct = s["answerable"]["answered"]["n"] + s["unanswerable"]["abstained"]["n"]
        answered = [t for t in traces if t["status"] == "answered"]
        cites = statistics.mean(len(t["citations"]) for t in answered) if answered else 0
        human = None
        rp = root / tag / "review.json"
        if rp.exists() and reviewed(load(rp)):
            human = aggregate(cases if len(traces) == len(cases) else [c for c in cases if c["id"] in {t["query_id"] for t in traces}],
                              traces, load(rp))
            grades = [r["context_grade"] for r in load(rp) if r.get("context_grade") is not None]
            if grades:  # chấm context 0/1/2 (BENCHMARK.md mục 2)
                human["context_grade"] = {str(k): grades.count(k) for k in (0, 1, 2)} | {"N": len(grades)}
        row = {"tag": tag, "method": cfg["method"], "neighbors": cfg.get("neighbors"), "prompt": cfg.get("prompt", "v1"),
               "top_k": cfg["top_k"], "budget": cfg["budget_chars"], "max_searches": cfg["max_searches"],
               "hit1_orig": retr.get("hit1"), "hit3_orig": retr.get("evidence_hit3"),
               "first_search_hit3_agent": s["answerable"]["first_search_evidence_hit3"],
               "context_evidence_rate": s["answerable"]["context_evidence_rate"],
               "correct_behavior": {"n": correct, "N": s["n"] - len(s["errors"])},
               "answered": s["answerable"]["answered"], "abstained_unanswerable": s["unanswerable"]["abstained"],
               "errors": len(s["errors"]), "searches": s["searches_distribution"], "avg_citations": round(cites, 2),
               "avg_context_chars": round(statistics.mean(t.get("context_chars", 0) for t in traces)),
               "cost_usd": s["cost_usd"], "median_s": s["latency_s"]["median"], "tokens": s["tokens"], "human": human}
        out.append(row)
        for t in traces:
            per_q.setdefault(t["query_id"], {})[tag] = t["status"][:3] + ("" if not t.get("auto") else
                                                                         ("+ctx" if t["auto"]["context_has_evidence"] else "-ctx"))
        g = human["grounded_answer"] if human else None
        rows.append(f"| {tag} | {cfg['method']}{' +neighbors' if cfg.get('neighbors') else ''} · prompt {row['prompt']} | "
                    f"{f(row['hit1_orig'])} | {f(row['hit3_orig'])} | {f(row['first_search_hit3_agent'])} | "
                    f"{f(row['context_evidence_rate'])} | {f(row['correct_behavior'])} | {f(row['answered'])} | "
                    f"{f(row['abstained_unanswerable'])} | {row['avg_citations']} | {row['avg_context_chars']} | "
                    f"{(str(g['0'])+'/'+str(g['1'])+'/'+str(g['2'])+' · '+format(g['mean'], '.2f')) if g else 'chưa chấm'} | "
                    f"{f(human['citation_validity']) if human else 'chưa chấm'} | ${row['cost_usd']:.4f} | {row['median_s']} s |")

    md = [f"# So sánh cấu hình agent — {args.split}", "",
          "Hit@1/Hit@3 (query gốc) lấy từ `results/retrieval/<split>/methods` (cùng top-k 3, không qua LLM). "
          "Hit@3 lượt search đầu dùng query agent tự viết. Context Evidence Rate tính trên context cuối của agent. "
          "Grounded answer và citation hợp lệ chỉ có khi review.json đã được người chấm.", "",
          "| Cấu hình | Phương pháp | Hit@1 (query gốc) | Evidence Hit@3 (query gốc) | Hit@3 lượt search đầu | Context Evidence Rate | Hành vi đúng | Trả lời câu có đáp án | Từ chối câu thiếu evidence | Citation TB / câu | Context TB (ký tự) | Grounded 0/1/2 · TB | Citation hợp lệ | Chi phí | Median |",
          "|" + "---|" * 15, *rows, "", "## Từng câu (ans/abs, ±ctx = context có/không có evidence)", "",
          "| Câu | " + " | ".join(tags) + " |", "|" + "---|" * (len(tags) + 1)]
    ctx_rows = [f"| {r['tag']} | {r['human']['context_grade']['0']} | {r['human']['context_grade']['1']} | "
                f"{r['human']['context_grade']['2']} | {r['human']['context_grade']['N']} |"
                for r in out if r["human"] and "context_grade" in r["human"]]
    if ctx_rows:
        md[md.index("## Từng câu (ans/abs, ±ctx = context có/không có evidence)"):0] = [
            "## Chấm context (người chấm, 0/1/2)", "", "| Cấu hình | 0 | 1 | 2 | N |", "|---|---|---|---|---|", *ctx_rows, ""]
    for qid in sorted(per_q):
        vals = [per_q[qid].get(t, "") for t in tags]
        mark = " ⚠" if len(set(vals)) > 1 else ""
        md.append(f"| {qid}{mark} | " + " | ".join(vals) + " |")
    (root / "comparison.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (root / "comparison.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
