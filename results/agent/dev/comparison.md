# So sánh cấu hình agent — dev

Hit@1/Hit@3 (query gốc) lấy từ `results/retrieval/<split>/methods` (cùng top-k 3, không qua LLM). Hit@3 lượt search đầu dùng query agent tự viết. Context Evidence Rate tính trên context cuối của agent. Grounded answer và citation hợp lệ chỉ có khi review.json đã được người chấm.

| Cấu hình | Phương pháp | Hit@1 (query gốc) | Evidence Hit@3 (query gốc) | Hit@3 lượt search đầu | Context Evidence Rate | Hành vi đúng | Trả lời câu có đáp án | Từ chối câu thiếu evidence | Citation TB / câu | Context TB (ký tự) | Grounded 0/1/2 · TB | Citation hợp lệ | Chi phí | Median |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseline_dense | dense · prompt v1 | 16/18 | 18/18 | 17/18 | 17/18 | 20/21 | 17/18 | 3/3 | 2.18 | 3100 | 1/0/17 · 1.89 | 37/37 | $0.0195 | 5.02 s |
| baseline_dense_r2 | dense · prompt v1 | 16/18 | 18/18 | 17/18 | 17/18 | 20/21 | 17/18 | 3/3 | 2.06 | 3029 | chưa chấm | chưa chấm | $0.0190 | 6.39 s |
| bm25 | bm25 · prompt v1 | 17/18 | 18/18 | 17/18 | 17/18 | 20/21 | 17/18 | 3/3 | 2.24 | 3285 | chưa chấm | chưa chấm | $0.0198 | 4.96 s |
| dense_neighbors | dense +neighbors · prompt v1 | 16/18 | 18/18 | 17/18 | 18/18 | 21/21 | 18/18 | 3/3 | 2 | 4260 | chưa chấm | chưa chấm | $0.0207 | 5.06 s |
| dense_neighbors_precise | dense +neighbors · prompt v2_precise | 16/18 | 18/18 | 17/18 | 18/18 | 21/21 | 18/18 | 3/3 | 1.61 | 4154 | 0/0/18 · 2.00 | 29/29 | $0.0198 | 4.35 s |
| hybrid_rrf | hybrid_rrf · prompt v1 | 17/18 | 18/18 | 17/18 | 17/18 | 20/21 | 17/18 | 3/3 | 2.41 | 3174 | chưa chấm | chưa chấm | $0.0201 | 5.62 s |

## Từng câu (ans/abs, ±ctx = context có/không có evidence)

| Câu | baseline_dense | baseline_dense_r2 | bm25 | dense_neighbors | dense_neighbors_precise | hybrid_rrf |
|---|---|---|---|---|---|---|
| d01 | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx |
| d02 | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx |
| d03 | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx |
| d04 | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx |
| d05 | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx |
| d06 | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx |
| d07 | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx |
| d08 | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx |
| d09 | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx |
| d10 | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx |
| d11 | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx |
| d12 ⚠ | abs-ctx | abs-ctx | abs-ctx | ans+ctx | ans+ctx | abs-ctx |
| d13 | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx |
| d14 | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx |
| d15 | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx |
| d16 | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx |
| d17 | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx |
| d18 | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx | ans+ctx |
| u01 | abs | abs | abs | abs | abs | abs |
| u02 | abs | abs | abs | abs | abs | abs |
| u03 | abs | abs | abs | abs | abs | abs |
