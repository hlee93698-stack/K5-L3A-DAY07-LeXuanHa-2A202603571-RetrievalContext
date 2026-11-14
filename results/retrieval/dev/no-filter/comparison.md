# Retrieval dev — no-filter

Corpus: 340 chunk (lab06_C), embedding intfloat/multilingual-e5-base. Câu có đáp án: 18; câu thiếu bằng chứng (không vào mẫu số): 3. Setup (load model + index): 46.5s.

| Phương pháp | Filter | top-k | Budget (ký tự) | Hit@1 | Evidence Hit@3 | Hit@10 | MRR@10 | Context Evidence Rate | Median / p90 ms | Chi phí | Miss@3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| dense | không | 3 | 3000 | 15/18 (83%) | 18/18 (100%) | 18/18 (100%) | 0.907 | 18/18 (100%) | 273.3 / 390.7 | $0 | — |
| bm25 | không | 3 | 3000 | 16/18 (89%) | 18/18 (100%) | 18/18 (100%) | 0.935 | 18/18 (100%) | 7.6 / 13.6 | $0 | — |
| bm25_ngram2 | không | 3 | 3000 | 15/18 (83%) | 18/18 (100%) | 18/18 (100%) | 0.907 | 18/18 (100%) | 10.1 / 14.8 | $0 | — |
| hybrid_rrf | không | 3 | 3000 | 15/18 (83%) | 18/18 (100%) | 18/18 (100%) | 0.907 | 18/18 (100%) | 241.9 / 361.9 | $0 | — |
| hybrid_rrf_ngram2 | không | 3 | 3000 | 15/18 (83%) | 18/18 (100%) | 18/18 (100%) | 0.907 | 18/18 (100%) | 238.4 / 287.7 | $0 | — |
