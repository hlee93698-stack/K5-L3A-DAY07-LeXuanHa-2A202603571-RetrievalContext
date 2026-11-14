# Tiêu chí chọn cấu hình (ghi ngày 2026-11-14, TRƯỚC khi chạy các cấu hình thử nghiệm bước 4)

Chỉ dùng **dev** (18 câu có đáp án, 3 câu thiếu bằng chứng). Test không được chạy cho tới khi cấu hình được chốt ở file `SELECTION.md`.

## Thứ tự ưu tiên

1. **Hành vi đúng (tự động):** số câu có đáp án được trả lời + số câu thiếu bằng chứng bị từ chối, trên 21 câu dev. Không có lỗi hệ thống.
2. **Context Evidence Rate** (evidence gold nằm trong context cuối) trên 18 câu có đáp án.
3. **Grounded answer** trung bình /2 và **citation hợp lệ** do người chấm, trên các câu mà cấu hình ứng viên có câu trả lời khác baseline (baseline chấm toàn bộ dev).
4. **Chi phí** USD và **thời gian** trung vị mỗi câu: chỉ dùng để phá hòa. Chấp nhận tăng chi phí tối đa 2× baseline nếu tiêu chí 1–3 tốt hơn.
5. Hòa hoàn toàn: chọn cấu hình đơn giản hơn (ít thành phần hơn).

Chênh lệch ≤ 1 câu được coi là trong mức nhiễu của LLM (đo bằng một lần chạy lặp baseline), không đủ để chọn cấu hình phức tạp hơn.

## Cấu hình dự kiến

| Tag | Thay đổi so với baseline | Giả thuyết |
|---|---|---|
| `baseline_dense` | dense, top-k 3, budget 6000 ký tự, tối đa 3 search, prompt v1, effort medium | Baseline Day 6 |
| `baseline_dense_r2` | chạy lặp baseline | Đo nhiễu do LLM không tất định |
| `bm25` | phương pháp 2: lexical BM25 | Văn bản luật nhiều thuật ngữ cố định, khớp từ khóa có thể bằng dense với chi phí retrieval thấp hơn |
| `hybrid_rrf` | phương pháp 3: dense + BM25 hợp nhất RRF | Bổ sung cho nhau khi agent viết lại query |
| `dense_neighbors` | cải thiện 1: thêm chunk liền kề cùng Điều | Sửa lỗi d12 (Điều bị cắt làm 2 chunk; evidence ở chunk sau); đổi lại context dài hơn |
| `*_precise` | cải thiện 2: prompt v2 yêu cầu trả lời đúng trọng tâm, chỉ trích đoạn trực tiếp hỗ trợ | Giảm citation thừa (9/17 câu baseline trích 3 chunk) và ý phụ không cần thiết |
