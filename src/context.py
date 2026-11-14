"""Đóng gói context gửi model: dedup theo chunk ID, giữ thứ tự xếp hạng, giới hạn theo ký tự.

Mỗi block có header [chunk-id | văn bản | trang] để model trích citation và người chấm đối chiếu.
Chunk không vừa budget bị bỏ qua (không cắt giữa chừng) và được ghi vào `dropped`.
"""
from __future__ import annotations

from typing import Any


def block(c: dict[str, Any]) -> str:
    m = c.get("metadata", {})
    pages = m.get("pages") or str(c["page"])
    name = m.get("short_name") or c["source_id"]
    return f"[{c['id']} | {name} | trang {pages}]\n{c['text']}"


def pack_context(results: list[dict[str, Any]], budget_chars: int = 3000) -> dict[str, Any]:
    blocks, ids, dropped, seen = [], [], [], set()
    for c in results:
        if c["id"] in seen:
            continue
        seen.add(c["id"])
        b = block(c)
        if len("\n\n".join(blocks + [b])) <= budget_chars:
            blocks.append(b)
            ids.append(c["id"])
        else:
            dropped.append(c["id"])
    text = "\n\n".join(blocks)
    return {"context": text, "context_ids": ids, "dropped_ids": dropped, "context_chars": len(text),
            "budget_chars": budget_chars}
