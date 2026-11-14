# Retrieval test — methods

Corpus: 340 chunk (lab06_C), embedding intfloat/multilingual-e5-base. Câu có đáp án: 6; câu thiếu bằng chứng (không vào mẫu số): 3. Setup (load model + index): 19.8s.

| Phương pháp | Filter | top-k | Budget (ký tự) | Hit@1 | Evidence Hit@3 | Hit@10 | MRR@10 | Context Evidence Rate | Median / p90 ms | Chi phí | Miss@3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| dense | có | 3 | 3000 | 6/6 (100%) | 6/6 (100%) | 6/6 (100%) | 1.000 | 6/6 (100%) | 80.3 / 108.3 | $0 | — |
