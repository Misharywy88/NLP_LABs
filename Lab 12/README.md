# Lab 12 — Transformers

Explores a pretrained Transformer with Hugging Face: tokenization, embeddings, self-attention weights and sentiment classification with DistilBERT (SST-2). The task loads `bert-base-uncased`, reports its 12 layers × 12 heads (144 heads in total), extracts the attention matrix from layer 3, head 2 for *"Transformers use self-attention to understand language."*, shows it as a table and heatmap, and explains what the rows (query tokens) and columns (key tokens) represent.

## Run the notebook

Use a Python virtual environment, install the dependencies, open `Lab12_Transformers.ipynb` and choose **Run All**. The first run downloads the models from Hugging Face.

```shell
python -m pip install transformers torch matplotlib seaborn pandas ipykernel
```
