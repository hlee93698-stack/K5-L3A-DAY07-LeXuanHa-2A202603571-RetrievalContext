# Cấu hình đã chốt (ghi ngày 2026-11-14, TRƯỚC khi chạy test)

**`dense_neighbors_precise`** — dense retrieval (e5 + Chroma `lab06_C`), thêm chunk liền kề cùng Điều, top-k 3, budget 6000 ký tự, tối đa 3 search, prompt `v2_precise`, `claude-haiku-5-5` effort medium.

Lệnh chạy test (giữ nguyên tham số):

```bash
python -m src.run_agent --split test --tag baseline_dense --method dense --top-k 3 --budget 6000 --max-searches 3
python -m src.run_agent --split test --tag dense_neighbors_precise --method dense --neighbors --prompt v2_precise --top-k 3 --budget 6000 --max-searches 3
```

## Áp dụng tiêu chí (SELECTION_CRITERIA.md) trên dev

| Tiêu chí | baseline_dense | dense_neighbors | dense_neighbors_precise | Các cấu hình khác |
|---|---|---|---|---|
| 1. Hành vi đúng | 20/21 | **21/21** | **21/21** | 20/21 (r2, bm25, hybrid_rrf) |
| 2. Context Evidence Rate | 17/18 | **18/18** | **18/18** | 17/18 |
| 3. Grounded answer (người chấm) | 1.89 (17×2, 1×0); citation 37/37; abstention 3/3 | chưa chấm | **2.00 (18×2)**; citation **29/29**; abstention 3/3 | — |
| 4. Chi phí · median | $0.0195 · 5.0 s | $0.0207 · 5.1 s | **$0.0198 · 4.4 s** | — |

Tiêu chí 1–2 loại các cấu hình không có neighbors. Giữa hai ứng viên còn lại, `dense_neighbors_precise` có nhãn người chấm không thấp hơn baseline (2.00 ≥ 1.89, citation 29/29), và tiêu chí 4 nghiêng về nó (rẻ hơn 4%, nhanh hơn 0.7 s). `dense_neighbors` không được chấm toàn bộ vì tiêu chí 4 đã quyết định.

Lưu ý khi đọc kết quả: hơn baseline 1 câu (d12) là mức chênh lệch nhỏ trên dev 21 câu; lý do chọn dựa trên nguyên nhân lỗi đã phân tích (Điều bị cắt làm hai chunk), không chỉ trên con số.

Không thay đổi tham số nào sau thời điểm này. Nếu test được dùng để chỉnh tiếp, phải tạo test mới.
