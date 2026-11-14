"""Kiểm tra vòng lặp agent bằng client giả (không gọi API; không phải benchmark)."""
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace as NS

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.agent import Agent, AgentConfig, Neighbors  # noqa: E402


def chunk(id, text, art=1, start=0):
    return {"id": id, "text": text, "source_id": "a", "source": "x://a", "page": 1,
            "metadata": {"document_id": "a", "page": 1, "page_end": 1, "pages": "1", "article": art,
                         "char_start": start, "short_name": "Luật A"}}


CH = [chunk("k1", "Điều 1. Thông báo.", 1, 0), chunk("k2", "Gửi trước 03 ngày làm việc.", 1, 100),
      chunk("k3", "Điều 2. Khác.", 2, 200)]


class FakeRetriever:
    name = "fake"

    def __init__(self, ids):
        self.ids = ids

    def search(self, query, *, filters=None, top_k=3):
        by = {c["id"]: c for c in CH}
        return [{**by[i], "score": 1.0, "rank": r, "method": "fake"} for r, i in enumerate(self.ids[:top_k], 1)]


def tool(name, inp, id="t"):
    return NS(type="tool_use", name=name, input=inp, id=id)


class FakeClient:
    def __init__(self, turns):
        self.turns, self.calls = list(turns), []
        self.messages = self

    def create(self, **kw):
        self.calls.append(kw)
        content = self.turns.pop(0)
        stop = "tool_use" if any(b.type == "tool_use" for b in content) else "end_turn"
        return NS(content=content, stop_reason=stop, usage=NS(input_tokens=10, output_tokens=5))


class AgentLoopTest(unittest.TestCase):
    def run_agent(self, turns, ids=("k1",), **cfg):
        client = FakeClient(turns)
        agent = Agent(FakeRetriever(list(ids)), AgentConfig(**cfg), CH, client=client)
        return agent.run("Gửi thông báo trước bao lâu?"), client

    def test_answer_with_alias_citation_maps_to_chunk_id(self):
        out, client = self.run_agent([[tool("search_documents", {"query": "thông báo"})],
                                      [tool("submit_answer", {"status": "answered", "answer": "Điều 1 [C1].", "citations": ["C1"]})]])
        self.assertEqual(out["status"], "answered")
        self.assertEqual(out["citations"], ["k1"])
        self.assertIn("[k1]", out["answer"])
        self.assertNotIn("gold", str(client.calls[0]["messages"]))

    def test_unknown_citation_abstains(self):
        out, _ = self.run_agent([[tool("search_documents", {"query": "x"})],
                                 [tool("submit_answer", {"status": "answered", "answer": "Sai [C9].", "citations": ["C9"]})]])
        self.assertEqual(out["status"], "abstain")
        self.assertTrue(out["stop_reason"].startswith("invalid_or_missing_citations"))

    def test_insufficient_evidence_and_search_limit(self):
        out, _ = self.run_agent([[tool("search_documents", {"query": "a"})], [tool("search_documents", {"query": "b"})],
                                 [tool("submit_answer", {"status": "insufficient_evidence", "answer": "Không đủ.", "citations": []})]],
                                max_searches=1)
        self.assertEqual(out["status"], "abstain")
        self.assertEqual(out["n_searches"], 1)
        self.assertTrue(any(e["event"] == "search_limit" for e in out["events"]))

    def test_neighbors_add_same_article_only(self):
        n = Neighbors(CH)
        self.assertEqual([c["id"] for c in n.of("k1")], ["k2"])
        out, _ = self.run_agent([[tool("search_documents", {"query": "x"})],
                                 [tool("submit_answer", {"status": "answered", "answer": "03 ngày [C2].", "citations": ["C2"]})]],
                                neighbors=True)
        self.assertEqual(out["citations"], ["k2"])

    def test_budget_drops_chunks(self):
        out, _ = self.run_agent([[tool("search_documents", {"query": "x"})],
                                 [tool("submit_answer", {"status": "insufficient_evidence", "answer": "-", "citations": []})]],
                                ids=("k1", "k2"), budget_chars=60)
        self.assertEqual(len(out["context_ids"]), 1)
        self.assertEqual(len(out["events"][0]["dropped_by_budget"]), 1)


if __name__ == "__main__":
    unittest.main()
