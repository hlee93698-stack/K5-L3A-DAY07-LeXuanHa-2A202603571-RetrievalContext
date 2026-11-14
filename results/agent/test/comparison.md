# So sánh cấu hình agent — test

Hit@1/Hit@3 (query gốc) lấy từ `results/retrieval/<split>/methods` (cùng top-k 3, không qua LLM). Hit@3 lượt search đầu dùng query agent tự viết. Context Evidence Rate tính trên context cuối của agent. Grounded answer và citation hợp lệ chỉ có khi review.json đã được người chấm.

| Cấu hình | Phương pháp | Hit@1 (query gốc) | Evidence Hit@3 (query gốc) | Hit@3 lượt search đầu | Context Evidence Rate | Hành vi đúng | Trả lời câu có đáp án | Từ chối câu thiếu evidence | Citation TB / câu | Context TB (ký tự) | Grounded 0/1/2 · TB | Citation hợp lệ | Chi phí | Median |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseline_dense | dense · prompt v1 | 6/6 | 6/6 | 6/6 | 6/6 | 9/9 | 6/6 | 3/3 | 2 | 3469 | 0/0/6 · 2.00 | 12/12 | $0.0092 | 4.84 s |
| dense_neighbors_precise | dense +neighbors · prompt v2_precise | 6/6 | 6/6 | 6/6 | 6/6 | 9/9 | 6/6 | 3/3 | 1.67 | 4667 | 0/0/6 · 2.00 | 10/10 | $0.0105 | 4.72 s |

## Chấm context (người chấm, 0/1/2)

| Cấu hình | 0 | 1 | 2 | N |
|---|---|---|---|---|
| baseline_dense | 0 | 0 | 6 | 6 |
| dense_neighbors_precise | 0 | 0 | 6 | 6 |

## Từng câu (ans/abs, ±ctx = context có/không có evidence)

| Câu | baseline_dense | dense_neighbors_precise |
|---|---|---|
| t01 | ans+ctx | ans+ctx |
| t02 | ans+ctx | ans+ctx |
| t03 | ans+ctx | ans+ctx |
| t04 | ans+ctx | ans+ctx |
| t05 | ans+ctx | ans+ctx |
| t06 | ans+ctx | ans+ctx |
| u04 | abs | abs |
| u05 | abs | abs |
| u06 | abs | abs |
