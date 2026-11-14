"""Unit test cho src/ (không load model, không gọi API)."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.context import pack_context  # noqa: E402
from src.evidence import chunk_hits  # noqa: E402
from src.retrieval import BM25Retriever, HybridRRF, matches, tokenize  # noqa: E402


def chunk(id, text, src="a", page=1, page_end=None, regime="2023"):
    return {"id": id, "text": text, "source_id": src, "source": f"x://{src}", "page": page,
            "metadata": {"document_id": src, "page": page, "page_end": page_end or page, "legal_regime": regime}}


CHUNKS = [chunk("c1", "Hoàn tiền trong 7 ngày làm việc.", regime="2023"),
          chunk("c2", "Bảo hành sản phẩm hàng hóa.", regime="2010"),
          chunk("c3", "Người tiêu dùng được hoàn tiền khi hủy dịch vụ.", page=2, page_end=3)]


class FakeRetriever:
    def __init__(self, name, ids):
        self.name, self.ids = name, ids

    def search(self, query, *, filters=None, top_k=3):
        by = {c["id"]: c for c in CHUNKS}
        return [{**by[i], "score": 1.0, "rank": r, "method": self.name} for r, i in enumerate(self.ids[:top_k], 1)]


class RetrievalTest(unittest.TestCase):
    def test_tokenize_bigram(self):
        self.assertEqual(tokenize("Người Tiêu dùng", 2), ["người", "tiêu", "dùng", "người_tiêu", "tiêu_dùng"])

    def test_bm25_ranks_and_filters(self):
        bm = BM25Retriever(CHUNKS)
        res = bm.search("hoàn tiền", top_k=3)
        self.assertEqual({r["id"] for r in res}, {"c1", "c3"})
        self.assertEqual([r["rank"] for r in res], [1, 2])
        self.assertEqual(bm.search("bảo hành", filters={"legal_regime": "2023"}), [])
        with self.assertRaises(ValueError):
            bm.search("x", filters={"gold": 1})

    def test_rrf_fuses_by_rank(self):
        h = HybridRRF([FakeRetriever("a", ["c1", "c2"]), FakeRetriever("b", ["c2", "c3"])], k=60)
        res = h.search("q", top_k=3)
        self.assertEqual(res[0]["id"], "c2")  # có mặt ở cả hai danh sách
        self.assertEqual(set(res[0]["components"]), {"a", "b"})

    def test_evidence_hit_page_span_and_fragments(self):
        gold = [{"source_id": "a", "page": 3, "evidence": ["hoàn  tiền", "HỦY dịch vụ"]}]
        self.assertTrue(chunk_hits(CHUNKS[2], gold))
        self.assertFalse(chunk_hits(CHUNKS[0], gold))

    def test_pack_context_dedup_and_budget(self):
        ctx = pack_context([CHUNKS[0], CHUNKS[0], CHUNKS[1]], budget_chars=80)
        self.assertEqual(ctx["context_ids"], ["c1"])
        self.assertEqual(ctx["dropped_ids"], ["c2"])
        self.assertLessEqual(ctx["context_chars"], 80)

    def test_filter_alias(self):
        self.assertTrue(matches(CHUNKS[0], {"source_id": "a"}))

    def test_benchmark_shape(self):
        path = ROOT / "data" / "benchmark" / "questions.json"
        if not path.exists():
            self.skipTest("chưa chạy python -m src.prepare_data")
        qs = json.loads(path.read_text(encoding="utf-8"))
        count = lambda s, a: sum(q["split"] == s and q["answerable"] == a for q in qs)  # noqa: E731
        self.assertGreaterEqual(count("dev", True), 15)
        self.assertGreaterEqual(count("dev", False), 2)
        self.assertGreaterEqual(count("test", True), 5)
        self.assertGreaterEqual(count("test", False), 2)
        for q in qs:
            self.assertNotIn("gold", q) if not q["answerable"] else self.assertTrue(q["gold"])


if __name__ == "__main__":
    unittest.main()
