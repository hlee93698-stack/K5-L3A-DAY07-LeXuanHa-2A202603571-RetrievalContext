"""Kiểm tra kết nối trước khi làm lab: Claude API, Chroma Day 6, embedding.

Chạy từ thư mục gốc:  python scripts/check_setup.py [--skip-llm] [--skip-embedding]
Không in API key. Lỗi được báo thật, không thay bằng kết quả giả.
"""
import argparse
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src import config  # noqa: E402


def check_llm() -> bool:
    import anthropic

    if not os.getenv("ANTHROPIC_API_KEY"):
        print("[LLM] FAIL: chưa có ANTHROPIC_API_KEY trong .env")
        return False
    client = anthropic.Anthropic()
    t0 = time.perf_counter()
    try:
        resp = client.messages.create(
            model=config.LLM_MODEL,
            max_tokens=256,
            output_config={"effort": "low"},
            messages=[{"role": "user", "content": "Trả lời đúng một từ: OK"}],
        )
    except anthropic.AuthenticationError as e:
        print(f"[LLM] FAIL 401: key không hợp lệ hoặc hết hạn ({e.message})")
        return False
    except anthropic.PermissionDeniedError as e:
        print(f"[LLM] FAIL 403: key không có quyền dùng model này ({e.message})")
        return False
    except anthropic.NotFoundError as e:
        print(f"[LLM] FAIL 404: model '{config.LLM_MODEL}' không tồn tại ({e.message})")
        return False
    except anthropic.RateLimitError as e:
        print(f"[LLM] FAIL 429: bị giới hạn tốc độ / hết credit ({e.message})")
        return False
    except anthropic.APIStatusError as e:
        print(f"[LLM] FAIL {e.status_code}: {e.message}")
        return False
    except anthropic.APIConnectionError as e:
        print(f"[LLM] FAIL: không kết nối được API ({e})")
        return False
    text = "".join(b.text for b in resp.content if b.type == "text").strip()
    u = resp.usage
    print(f"[LLM] OK model={resp.model} stop={resp.stop_reason} reply={text!r} "
          f"tokens in/out={u.input_tokens}/{u.output_tokens} {time.perf_counter() - t0:.1f}s")
    return True


def check_chroma():
    import chromadb

    if not config.DAY6_CHROMA_PATH.exists():
        print(f"[Chroma] FAIL: không thấy {config.DAY6_CHROMA_PATH}")
        return None
    client = chromadb.PersistentClient(path=str(config.DAY6_CHROMA_PATH))
    names = [c.name for c in client.list_collections()]
    if config.DAY6_COLLECTION not in names:
        print(f"[Chroma] FAIL: thiếu collection {config.DAY6_COLLECTION}; có: {names}")
        return None
    col = client.get_collection(config.DAY6_COLLECTION)
    print(f"[Chroma] OK collections={names} {config.DAY6_COLLECTION}: {col.count()} chunk, "
          f"metadata={col.metadata}")
    return col


def check_embedding(col) -> bool:
    from sentence_transformers import SentenceTransformer

    t0 = time.perf_counter()
    model = SentenceTransformer(config.EMBEDDING_MODEL, revision=config.EMBEDDING_REVISION, device="cpu")
    q = "Ngày Quyền của người tiêu dùng Việt Nam là ngày nào?"
    vec = model.encode([config.QUERY_PREFIX + q], normalize_embeddings=True)[0]
    print(f"[Embedding] OK {config.EMBEDDING_MODEL} dim={len(vec)} load+encode {time.perf_counter() - t0:.1f}s")
    if col is None:
        return True
    res = col.query(query_embeddings=[vec.tolist()], n_results=3)
    print(f"[Dense] query thử: {q}")
    for cid, dist, meta in zip(res["ids"][0], res["distances"][0], res["metadatas"][0]):
        print(f"   {cid}  cos_dist={dist:.4f}  page={meta.get('page')}  src={meta.get('document_id', meta.get('source'))}")
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-llm", action="store_true")
    ap.add_argument("--skip-embedding", action="store_true")
    args = ap.parse_args()
    ok = True
    if not args.skip_llm:
        ok &= check_llm()
    col = check_chroma()
    ok &= col is not None
    if not args.skip_embedding:
        ok &= check_embedding(col)
    print("=> TẤT CẢ OK" if ok else "=> CÓ LỖI, xem ở trên")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
