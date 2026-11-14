# Thử nghiệm trên dev (bước 4)

Tiêu chí chọn đã ghi trước khi chạy: [SELECTION_CRITERIA.md](SELECTION_CRITERIA.md). Bảng đầy đủ: [comparison.md](comparison.md) (tạo bằng `python -m src.compare_agent --split dev`).
Model `claude-haiku-5-5`, effort medium; top-k 3, budget 6000 ký tự, tối đa 3 search cho mọi cấu hình. Dev: 18 câu có đáp án + 3 câu thiếu bằng chứng. Mỗi cấu hình chạy 1 lần, baseline chạy 2 lần để đo nhiễu.

## Kết quả

| Cấu hình | Vai trò | Hit@1 / Hit@3 (query gốc) | Context Evidence Rate | Hành vi đúng | Citation TB | Độ dài trả lời TB (ký tự) | Grounded (người chấm) | Chi phí / median |
|---|---|---|---|---|---|---|---|---|
| baseline_dense | baseline (phương pháp 1) | 16/18 · 18/18 | 17/18 | 20/21 | 2.18 | 613 | 1.89 (17×2, 1×0); citation 37/37 | $0.0195 · 5.0 s |
| baseline_dense_r2 | đo nhiễu | 16/18 · 18/18 | 17/18 | 20/21 | 2.06 | 582 | — | $0.0190 · 6.4 s |
| bm25 | phương pháp 2 | 17/18 · 18/18 | 17/18 | 20/21 | 2.24 | 575 | — | $0.0198 · 5.0 s |
| hybrid_rrf | phương pháp 3 | 17/18 · 18/18 | 17/18 | 20/21 | 2.41 | 653 | — | $0.0201 · 5.6 s |
| dense_neighbors | cải thiện 1 | 16/18 · 18/18 | **18/18** | **21/21** | 2.00 | 562 | — | $0.0207 · 5.1 s |
| dense_neighbors_precise | cải thiện 2 (trên cải thiện 1) | 16/18 · 18/18 | **18/18** | **21/21** | **1.61** | **360** | **2.00 (18×2); citation 29/29** | **$0.0198 · 4.4 s** |

Nhãn người chấm: `baseline_dense/review.json`, `dense_neighbors_precise/review.json` (đã đối chiếu từng citation với nguyên văn chunk). Ý phụ "văn bản cũ đã hết hiệu lực" không có citation hỗ trợ: 6/17 câu baseline, 3/18 câu cấu hình chọn — ghi chú trong lý do, không trừ điểm vì không làm sai đáp án chính.

Nhiễu LLM: hai lần chạy baseline giống hệt nhau về trạng thái từng câu; citation TB 2.18 và 2.06; số câu trả lời có ý phụ "hết hiệu lực/đã được thay thế" là 7 và 4.

## Phân tích lỗi dev

**Lỗi 1 — d12, từ chối nhầm (mọi cấu hình không có neighbors).**
Câu hỏi: thông báo bán hàng không tại địa điểm giao dịch thường xuyên phải gửi UBND cấp xã trước bao lâu (đáp án: tối thiểu 03 ngày làm việc, NĐ 55/2024 Điều 26 khoản 3, trang 19).
Nguyên nhân: chunking theo cấu trúc của Day 6 cắt Điều 26 làm hai chunk. Chunk đầu (khoản 1–2, trang 18) chứa tiêu đề Điều nên luôn xếp hạng 1; con số nằm ở chunk sau (khoản 3, trang 19). Khi chỉ dùng câu hỏi gốc, retrieval vẫn đưa chunk này lên hạng 3; nhưng agent tự viết lại query và cả 3 lượt tìm đều không lấy được nó. Đổi phương pháp retrieval (bm25, hybrid) không sửa được.
Giả thuyết: thêm chunk liền kề cùng Điều vào context sẽ đưa evidence vào mà không phụ thuộc query.
Kết quả: `dense_neighbors` trả lời đúng d12, có citation đúng chunk evidence; Context Evidence Rate 17/18 → 18/18. Đổi lại context dài hơn 37% (3100 → 4260 ký tự), chi phí +6%.

**Lỗi 2 — câu trả lời dài, thêm ý phụ và citation thừa (baseline).**
6/17 câu trả lời trích ≥3 chunk; 10/17 có đoạn "Lưu ý"; 7/17 nêu văn bản cũ "đã hết hiệu lực" mà không trích chunk hỗ trợ. Ý này đúng (Điều 79 Luật 19/2023, Điều 29 NĐ 55/2024 có trong corpus) nhưng đến từ system prompt, không từ context được trích → câu trả lời không hoàn toàn grounded vào citation.
Giả thuyết: yêu cầu trả lời đúng trọng tâm, chỉ trích đoạn trực tiếp hỗ trợ sẽ giảm citation và ý phụ mà không giảm độ đúng.
Kết quả: citation TB 2.00 → 1.61, câu ≥3 citation 4 → 2, độ dài 562 → 360 ký tự, câu TB 3.3 → 1.9, chi phí −4%, median 5.1 → 4.4 s; hành vi đúng giữ 21/21. Số câu nêu "hết hiệu lực" 5 → 3 nằm trong mức nhiễu, chưa đủ để kết luận.

## Đánh đổi

- Phương pháp retrieval: trên dev này cả ba đều đạt Evidence Hit@3 18/18 với query gốc; BM25 nhỉnh hơn ở Hit@1 (17/18) và nhanh hơn ~35 lần (7 ms so với 266 ms) nhưng không đổi kết quả cuối của agent. Benchmark quá dễ để phân biệt phương pháp ở mức agent — đây là giới hạn cần nêu.
- Neighbors tăng context và token đầu vào; với Haiku 5.5 mức tăng chi phí không đáng kể (+$0.0012 / 21 câu).
- Prompt v2 rẻ và nhanh hơn vì câu trả lời ngắn hơn.

## Chọn cấu hình

Đã chốt **`dense_neighbors_precise`** — xem [SELECTION.md](SELECTION.md).
