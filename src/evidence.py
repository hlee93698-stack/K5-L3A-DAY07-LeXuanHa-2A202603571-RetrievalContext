"""Định nghĩa hit dùng chung cho mọi phương pháp (giống Day 6 để so sánh được).

Một chunk *hit* một mục gold khi:
  * chunk.source_id == gold.source_id,
  * gold.page nằm trong [chunk.page, chunk.metadata.page_end], và
  * mọi đoạn evidence của mục gold nằm trong text chunk (sau NFC + lowercase + gộp khoảng trắng).
`gold.evidence` là chuỗi, hoặc danh sách chuỗi phải cùng nằm trong một chunk.
Các mục trong `gold` là evidence thay thế: hit bất kỳ mục nào là đủ.
"""
from __future__ import annotations

import re
import unicodedata
from typing import Any


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s).lower()).strip()


def fragments(gold: dict[str, Any]) -> list[str]:
    ev = gold["evidence"]
    return [ev] if isinstance(ev, str) else list(ev)


def page_span(chunk: dict[str, Any]) -> tuple[int, int]:
    start = int(chunk["page"])
    return start, int(chunk.get("metadata", {}).get("page_end", start))


def chunk_hits(chunk: dict[str, Any], gold: list[dict[str, Any]]) -> bool:
    start, end = page_span(chunk)
    text = norm(chunk["text"])
    return any(chunk["source_id"] == g["source_id"] and start <= int(g["page"]) <= end
               and all(norm(f) in text for f in fragments(g)) for g in gold)
