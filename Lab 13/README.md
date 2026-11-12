# Lab 13 — Information Retrieval for RAG

Sparse (TF-IDF + cosine similarity) retrieval over a small set of NLP course notes.

- `Lab_13_Part_1_Information_Retrieval_for_RAG.ipynb` — TF-IDF vectors, query scoring, top-k ranking, exercises (NER query, `k=1` vs `k=3`) with a score bar chart.
- `Lab_13_Part_2_Search_and_Retrieval.ipynb` — reusable `search()`, zero-score filtering, sparse vs dense comparison, and practice questions (adding a BERT note and rebuilding the index).

## Run the notebooks

Use a Python 3.12 kernel, install the dependencies, open each notebook and choose **Run All**.

```shell
python -m pip install scikit-learn pandas matplotlib ipykernel
```
