# Lab 11 — Attention with an RNN

Train a question-to-answer-group classifier on the supplied CSV. The notebook plots attention for three questions from different groups and compares two versions of a question about getting hurt. Bars correspond to actual tokens, and padding receives zero attention.

## Run the notebook

Open this folder in VS Code with the Python and Jupyter extensions. Use a Python 3.12 kernel. Install the dependencies in that environment, then open `Lab11_Completed.ipynb` and choose **Run All**.

```shell
python -m pip install pandas torch tensorflow matplotlib ipykernel
```

The visualizations describe this trained model on examples from its training data. They do not measure performance on unseen questions.
