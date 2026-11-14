"""Các phương pháp retrieval Day 7, cùng một interface:

    retriever.search(query, filters=None, top_k=3) -> list[dict]

Mỗi kết quả: id, text, source_id, source, page, metadata, score, rank, method.
`filters` chỉ nhận từ người dùng/benchmark (vd {"legal_regime": "2010"}), không suy từ gold.
Lỗi model/vector store được raise, không có fallback giả.
"""
from __future__ import annotations

import json
import math
import re
import time
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Any, Protocol

from src import config

CORPUS_PATH = config.ROOT / "data" / "corpus" / "chunks.json"
ALLOWED_FILTER_FIELDS = {"legal_regime", "document_type", "source_id", "document_id"}


class Retriever(Protocol):
    name: str

    def search(self, query: str, *, filters: dict[str, Any] | None = None, top_k: int = 3) -> list[dict[str, Any]]: ...


def load_chunks(path: Path = CORPUS_PATH) -> list[dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def _check_filters(filters: dict[str, Any] | None) -> dict[str, Any]:
    filters = dict(filters or {})
    bad = set(filters) - ALLOWED_FILTER_FIELDS
    if bad:
        raise ValueError(f"filter không hỗ trợ: {sorted(bad)}")
    if "source_id" in filters:  # tên trường trong metadata Day 6
        filters["document_id"] = filters.pop("source_id")
    return filters


def matches(chunk: dict[str, Any], filters: dict[str, Any] | None) -> bool:
    return all(str(chunk["metadata"].get(k)) == str(v) for k, v in _check_filters(filters).items())


def _result(chunk: dict[str, Any], score: float, rank: int, method: str, **extra) -> dict[str, Any]:
    return {**chunk, "score": float(score), "rank": rank, "method": method, **extra}


# ---------------------------------------------------------------- lexical
def tokenize(text: str, ngram: int = 1) -> list[str]:
    """Tách âm tiết (\\w+ sau NFC + casefold). ngram=2 thêm cặp âm tiết liền kề
    ("người_tiêu", "tiêu_dùng") để xấp xỉ từ ghép tiếng Việt khi không dùng word segmenter."""
    syl = re.findall(r"\w+", unicodedata.normalize("NFC", text).casefold())
    if ngram < 2:
        return syl
    return syl + [f"{a}_{b}" for a, b in zip(syl, syl[1:])]


class BM25Retriever:
    def __init__(self, chunks: list[dict[str, Any]], *, k1: float = 1.5, b: float = 0.75, ngram: int = 1):
        self.chunks, self.k1, self.b, self.ngram = chunks, k1, b, ngram
        self.name = "bm25" if ngram == 1 else f"bm25_ngram{ngram}"
        t0 = time.perf_counter()
        self.tf = [Counter(tokenize(c["text"], ngram)) for c in chunks]
        self.len = [sum(tf.values()) for tf in self.tf]
        self.avgdl = sum(self.len) / len(self.len)
        df = Counter(t for tf in self.tf for t in tf)
        n = len(chunks)
        self.idf = {t: math.log(1 + (n - d + 0.5) / (d + 0.5)) for t, d in df.items()}
        self.index_seconds = time.perf_counter() - t0

    def score(self, i: int, q_terms: list[str]) -> float:
        tf, dl, s = self.tf[i], self.len[i], 0.0
        for t in q_terms:
            f = tf.get(t)
            if f:
                s += self.idf[t] * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * dl / self.avgdl))
        return s

    def search(self, query, *, filters=None, top_k=3):
        q_terms = tokenize(query, self.ngram)
        scored = [(self.score(i, q_terms), c) for i, c in enumerate(self.chunks) if matches(c, filters)]
        scored = sorted((x for x in scored if x[0] > 0), key=lambda x: (-x[0], x[1]["id"]))[:top_k]
        return [_result(c, s, r, self.name) for r, (s, c) in enumerate(scored, 1)]


# ---------------------------------------------------------------- dense
class DenseRetriever:
    """Query embedding e5 ("query: " + câu hỏi, normalize) -> Chroma collection Day 6 (cosine HNSW)."""

    name = "dense"

    def __init__(self, chunks: list[dict[str, Any]] | None = None):
        import chromadb
        from sentence_transformers import SentenceTransformer

        t0 = time.perf_counter()
        self.model = SentenceTransformer(config.EMBEDDING_MODEL, revision=config.EMBEDDING_REVISION, device="cpu")
        self.model_load_seconds = time.perf_counter() - t0
        self.col = chromadb.PersistentClient(path=str(config.DAY6_CHROMA_PATH)).get_collection(config.DAY6_COLLECTION)
        meta = self.col.metadata or {}
        if meta.get("embedding_model") not in (None, config.EMBEDDING_MODEL):
            raise ValueError(f"collection dùng {meta.get('embedding_model')}, query dùng {config.EMBEDDING_MODEL}")
        self.dim = self.model.get_embedding_dimension()
        self.by_id = {c["id"]: c for c in (chunks or load_chunks())}

    def embed(self, query: str) -> list[float]:
        return self.model.encode([config.QUERY_PREFIX + query], normalize_embeddings=True)[0].tolist()

    def search(self, query, *, filters=None, top_k=3):
        f = _check_filters(filters)
        clauses = [{k: {"$eq": v}} for k, v in f.items()]
        where = None if not clauses else clauses[0] if len(clauses) == 1 else {"$and": clauses}
        res = self.col.query(query_embeddings=[self.embed(query)], n_results=top_k, where=where,
                             include=["distances"])
        out = []
        for r, (cid, dist) in enumerate(zip(res["ids"][0], res["distances"][0]), 1):
            if cid not in self.by_id:
                raise KeyError(f"chunk {cid} có trong Chroma nhưng không có trong corpus export")
            out.append(_result(self.by_id[cid], 1.0 - dist, r, self.name, distance=float(dist)))
        return out


# ---------------------------------------------------------------- hybrid
class HybridRRF:
    """Reciprocal Rank Fusion: score = Σ 1/(k + rank_i). Không cộng trực tiếp score dense (cosine)
    và BM25 vì khác thang đo; RRF chỉ dùng thứ hạng nên không cần chuẩn hóa."""

    def __init__(self, retrievers: list[Retriever], *, k: int = 60, candidate_k: int = 20, name: str | None = None):
        self.retrievers, self.k, self.candidate_k = retrievers, k, candidate_k
        self.name = name or "hybrid_rrf(" + "+".join(r.name for r in retrievers) + ")"

    def search(self, query, *, filters=None, top_k=3):
        fused: dict[str, dict[str, Any]] = {}
        for ret in self.retrievers:
            for hit in ret.search(query, filters=filters, top_k=self.candidate_k):
                e = fused.setdefault(hit["id"], {"chunk": hit, "score": 0.0, "components": {}})
                e["score"] += 1.0 / (self.k + hit["rank"])
                e["components"][ret.name] = {"rank": hit["rank"], "score": hit["score"]}
        ranked = sorted(fused.values(), key=lambda e: (-e["score"], e["chunk"]["id"]))[:top_k]
        out = []
        for r, e in enumerate(ranked, 1):
            base = {k: v for k, v in e["chunk"].items() if k not in ("score", "rank", "method", "distance")}
            out.append(_result(base, e["score"], r, self.name, components=e["components"]))
        return out


def build(names: list[str], chunks: list[dict[str, Any]] | None = None) -> dict[str, Retriever]:
    """Tạo retriever theo tên; dense chỉ load model một lần."""
    chunks = chunks or load_chunks()
    cache: dict[str, Retriever] = {}

    def get(n: str) -> Retriever:
        if n not in cache:
            if n == "dense":
                cache[n] = DenseRetriever(chunks)
            elif n == "bm25":
                cache[n] = BM25Retriever(chunks)
            elif n == "bm25_ngram2":
                cache[n] = BM25Retriever(chunks, ngram=2)
            elif n == "hybrid_rrf":
                cache[n] = HybridRRF([get("dense"), get("bm25")], name="hybrid_rrf")
            elif n == "hybrid_rrf_ngram2":
                cache[n] = HybridRRF([get("dense"), get("bm25_ngram2")], name="hybrid_rrf_ngram2")
            else:
                raise ValueError(f"phương pháp không biết: {n}")
        return cache[n]

    return {n: get(n) for n in names}
