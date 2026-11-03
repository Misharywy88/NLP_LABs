# Lab 7 — Transformer model families

Compare DistilGPT-2 generation, FLAN-T5 translation and summarization, and DistilBERT sentiment classification. The supplied notebook skips Task 4 in its numbering. All listed tasks and the optional sampling challenge are included.

## Run the notebook

Open this folder in VS Code with the Python and Jupyter extensions. Use a Python 3.12 kernel. Install the dependencies in that environment, then open `Lab7_Completed.ipynb` and choose **Run All**.

```shell
python -m pip install "transformers==4.57.3" torch sentencepiece protobuf ipykernel
```

The first run downloads the three public model checkpoints. The optional challenge intentionally samples without resetting the random seed.
