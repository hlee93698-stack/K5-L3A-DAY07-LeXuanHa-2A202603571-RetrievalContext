# Retrieval dev — methods

Corpus: 340 chunk (lab06_C), embedding intfloat/multilingual-e5-base. Câu có đáp án: 18; câu thiếu bằng chứng (không vào mẫu số): 3. Setup (load model + index): 50.9s.

| Phương pháp | Filter | top-k | Budget (ký tự) | Hit@1 | Evidence Hit@3 | Hit@10 | MRR@10 | Context Evidence Rate | Median / p90 ms | Chi phí | Miss@3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| dense | có | 3 | 3000 | 16/18 (89%) | 18/18 (100%) | 18/18 (100%) | 0.935 | 18/18 (100%) | 266.2 / 378.6 | $0 | — |
| bm25 | có | 3 | 3000 | 17/18 (94%) | 18/18 (100%) | 18/18 (100%) | 0.963 | 18/18 (100%) | 6.8 / 10.3 | $0 | — |
| bm25_ngram2 | có | 3 | 3000 | 16/18 (89%) | 18/18 (100%) | 18/18 (100%) | 0.935 | 18/18 (100%) | 9.2 / 14.1 | $0 | — |
| hybrid_rrf | có | 3 | 3000 | 17/18 (94%) | 18/18 (100%) | 18/18 (100%) | 0.963 | 18/18 (100%) | 306.0 / 608.6 | $0 | — |
| hybrid_rrf_ngram2 | có | 3 | 3000 | 16/18 (89%) | 18/18 (100%) | 18/18 (100%) | 0.935 | 18/18 (100%) | 239.0 / 304.5 | $0 | — |
