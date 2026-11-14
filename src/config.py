"""Cấu hình Day 7: đọc .env ở thư mục gốc repo. Không hardcode secret."""
import os
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")


def _path(name: str, default: str) -> Path:
    p = Path(os.getenv(name, default))
    return p if p.is_absolute() else (ROOT / p).resolve()


# LLM (Claude). SDK tự đọc ANTHROPIC_API_KEY từ môi trường.
LLM_MODEL = os.getenv("LLM_MODEL", "claude-haiku-5-5")
LLM_EFFORT = os.getenv("LLM_EFFORT", "medium")  # low | medium | high | xhigh | max

# Day 6: vector store + embedding (chạy local)
DAY6_ROOT = _path("DAY6_ROOT", "../K5-L3A-DAY06-LeXuanHa-2A202603571-DataIngestion")
DAY6_CHROMA_PATH = _path("DAY6_CHROMA_PATH", str(DAY6_ROOT / "starter" / "chroma_db"))
DAY6_COLLECTION = os.getenv("DAY6_COLLECTION", "lab06_C")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "intfloat/multilingual-e5-base")
EMBEDDING_REVISION = os.getenv("EMBEDDING_REVISION") or None
QUERY_PREFIX = "query: "      # e5 yêu cầu tiền tố, khớp với Day 6
PASSAGE_PREFIX = "passage: "
