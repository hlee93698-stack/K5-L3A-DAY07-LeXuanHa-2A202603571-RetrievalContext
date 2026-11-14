# Code

Python 3.11, dùng lại venv Day 6 (`../K5-L3A-DAY06-LeXuanHa-2A202603571-DataIngestion/starter/.venv`) + `pip install -r requirements.txt`.
Cấu hình trong `.env` (mẫu: `.env.example`). Chạy mọi lệnh từ thư mục gốc repo; trên Windows đặt `PYTHONUTF8=1`.

| File | Việc |
|---|---|
| `config.py` | Đọc `.env`: model Claude, đường dẫn Chroma Day 6, embedding |
| `prepare_data.py` | Bước 1: xuất 340 chunk `lab06_C` → `data/corpus/chunks.json`; chuyển 24 câu Day 6 + 6 câu thiếu bằng chứng (`data/benchmark/unanswerable.json`) → `data/benchmark/questions.json`, `cases.json`, `validation.json` |
| `evidence.py` | Định nghĩa hit (nguồn + trang trong [page, page_end] + evidence chuẩn hóa nằm trong chunk), giống Day 6 |
| `retrieval.py` | `dense` (e5 + Chroma), `bm25`, `bm25_ngram2` (thêm bigram âm tiết), `hybrid_rrf`, `hybrid_rrf_ngram2` |
| `context.py` | Đóng gói context: dedup, giữ thứ tự, budget theo ký tự, ghi chunk bị bỏ |
| `eval_retrieval.py` | Benchmark retrieval/context: Hit@1, Evidence Hit@3, Hit@10, MRR@10, Context Evidence Rate, thời gian |
| `agent.py` | Agent Claude (manual tool loop): `search_documents` + `submit_answer`, alias citation `C#`, context dedup + budget, tùy chọn chunk lân cận cùng Điều |
| `run_agent.py` | Chạy agent trên một split → `results/agent/<split>/<tag>/` (traces, summary, review.json để chấm tay, review_sheet.md) |

```bash
python scripts/check_setup.py                 # kiểm tra Claude API, Chroma, embedding
python -m src.prepare_data                    # bước 1
python -m src.eval_retrieval --split dev      # bước 2 (mặc định: dense, bm25, bm25_ngram2, hybrid_rrf)
python -m src.eval_retrieval --split dev --methods dense bm25 bm25_ngram2 hybrid_rrf hybrid_rrf_ngram2 --no-filter --tag no-filter
python -m unittest discover -s tests -v
```

Toàn bộ lần chạy agent trong báo cáo (cần `ANTHROPIC_API_KEY`; tổng ~$0.14 với `claude-haiku-5-5`). Tham số chung: `--top-k 3 --budget 6000 --max-searches 3`.

```bash
C="--top-k 3 --budget 6000 --max-searches 3"
# dev: 3 phương pháp + đo nhiễu + 2 cải thiện
python -m src.run_agent --split dev --tag baseline_dense          --method dense      $C
python -m src.run_agent --split dev --tag baseline_dense_r2       --method dense      $C
python -m src.run_agent --split dev --tag bm25                    --method bm25       $C
python -m src.run_agent --split dev --tag hybrid_rrf              --method hybrid_rrf $C
python -m src.run_agent --split dev --tag dense_neighbors         --method dense --neighbors $C
python -m src.run_agent --split dev --tag dense_neighbors_precise --method dense --neighbors --prompt v2_precise $C
python -m src.compare_agent --split dev
# test: chỉ sau khi chốt results/agent/dev/SELECTION.md
python -m src.eval_retrieval --split test --methods dense
python -m src.run_agent --split test --tag baseline_dense          --method dense $C
python -m src.run_agent --split test --tag dense_neighbors_precise --method dense --neighbors --prompt v2_precise $C
python -m src.compare_agent --split test
```

`run_agent` không ghi đè `review.json` đã có nhãn (ghi ra `review.template.json`). Kết quả LLM không tất định: chạy lại có thể khác vài câu về câu chữ/citation.

Kết quả: `results/retrieval/<split>/<tag>/<method>/{traces,summary}.json` và `comparison.md`.
Không chạy `--split test` trước khi chốt cấu hình trên dev.
