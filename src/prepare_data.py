"""Bước 1: xuất corpus từ vector store Day 6 và tạo benchmark Day 7.

    python -m src.prepare_data

Đầu ra:
  data/corpus/chunks.json          340 chunk của collection lab06_C (đúng nội dung đã index)
  data/benchmark/questions.json    toàn bộ câu dev/test (có đáp án + thiếu bằng chứng)
  data/benchmark/cases.json        id/split/answerable cho starter/agent_metrics.py
  data/benchmark/validation.json   kết quả kiểm tra gold và kiểm tra vắng mặt
Không gọi model nào; gold chỉ dùng để kiểm tra, không đi vào retrieval.
"""
from __future__ import annotations

import json
import os
from collections import Counter
from pathlib import Path

import chromadb

from src import config
from src.evidence import chunk_hits, norm


def rel(p) -> str:
    """Đường dẫn tương đối so với repo (không ghi đường dẫn máy cá nhân)."""
    return os.path.relpath(p, config.ROOT).replace(os.sep, "/")

DATA = config.ROOT / "data"
CORPUS = DATA / "corpus" / "chunks.json"
BENCH = DATA / "benchmark"


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def export_chunks() -> tuple[list[dict], dict]:
    client = chromadb.PersistentClient(path=str(config.DAY6_CHROMA_PATH))
    col = client.get_collection(config.DAY6_COLLECTION)
    got = col.get(include=["documents", "metadatas"])
    chunks = []
    for cid, text, meta in zip(got["ids"], got["documents"], got["metadatas"]):
        meta = dict(meta)
        chunks.append({"id": cid, "text": text, "source_id": meta["document_id"],
                       "source": meta["source"], "page": int(meta["page"]), "metadata": meta})
    chunks.sort(key=lambda c: (c["source_id"], c["page"], c["metadata"].get("char_start", 0), c["id"]))
    if len({c["id"] for c in chunks}) != len(chunks):
        raise ValueError("chunk ID trùng")
    info = {"collection": config.DAY6_COLLECTION, "chroma_path": rel(config.DAY6_CHROMA_PATH),
            "collection_metadata": col.metadata, "count": len(chunks),
            "by_source": dict(Counter(c["source_id"] for c in chunks))}
    return chunks, info


def convert_answerable(q: dict) -> dict:
    gold = [{"source_id": g["source_id"], "page": int(g["page"]), "evidence": g["evidence_quote"]}
            for g in q["gold"]]
    return {"id": q["id"], "split": q["split"], "type": q["type"], "question": q["question"],
            "answerable": True, "expected_behavior": "search_and_answer",
            "expected_answer": q["expected_answer"], "filter": q.get("filter"), "gold": gold}


def main() -> None:
    chunks, info = export_chunks()
    write_json(CORPUS, chunks)

    day6_q = config.DAY6_ROOT / "benchmark" / "questions.jsonl"
    answerable = [convert_answerable(json.loads(line))
                  for line in day6_q.read_text(encoding="utf-8").splitlines() if line.strip()]
    unanswerable = json.loads((BENCH / "unanswerable.json").read_text(encoding="utf-8"))

    report = {"corpus": info, "source_questions": rel(day6_q), "gold_check": [], "absence_check": []}
    for q in answerable:
        hits = [c["id"] for c in chunks if chunk_hits(c, q["gold"])]
        report["gold_check"].append({"id": q["id"], "hit_chunks": hits})
        if not hits:
            raise ValueError(f"{q['id']}: gold không nằm trọn trong chunk nào đúng nguồn/trang")

    texts = [norm(c["text"]) for c in chunks]
    for u in unanswerable:
        found = {t: sum(norm(t) in x for x in texts) for t in u["absence_check"]["terms"]}
        related = {t: sum(norm(t) in x for x in texts) for t in u["absence_check"].get("related_terms", [])}
        report["absence_check"].append({"id": u["id"], "terms_found": found, "related_terms_found": related})
        if any(found.values()):
            raise ValueError(f"{u['id']}: thuật ngữ được cho là vắng mặt lại có trong corpus: {found}")
        u.update({"answerable": False, "expected_behavior": "search_and_abstain", "filter": None})

    questions = answerable + unanswerable
    ids = [q["id"] for q in questions]
    if len(set(ids)) != len(ids):
        raise ValueError("question ID trùng")
    counts = Counter((q["split"], q["answerable"]) for q in questions)
    report["counts"] = {f"{s}_{'answerable' if a else 'unanswerable'}": n for (s, a), n in sorted(counts.items())}
    need = {("dev", True): 15, ("dev", False): 2, ("test", True): 5, ("test", False): 2}
    for key, minimum in need.items():
        if counts[key] < minimum:
            raise ValueError(f"benchmark thiếu câu {key}: {counts[key]} < {minimum}")

    write_json(BENCH / "questions.json", questions)
    write_json(BENCH / "cases.json", [{"id": q["id"], "split": q["split"], "answerable": q["answerable"]}
                                      for q in questions])
    write_json(BENCH / "validation.json", report)
    print(json.dumps({"chunks": info["count"], "by_source": info["by_source"], **report["counts"],
                      "gold_ok": len(answerable), "absence_ok": len(unanswerable)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
