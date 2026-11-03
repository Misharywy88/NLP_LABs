# Lab 8 — Part-of-speech tagging

Compare NLTK and spaCy tags, inspect how context changes the roles of “google” and “table”, and visualize the supplied sentences with displaCy.

## Run the notebook

Open this folder in VS Code with the Python and Jupyter extensions. Use a Python 3.12 kernel. Install the dependencies in that environment, then open `Lab8_Completed.ipynb` and choose **Run All**.

```shell
python -m pip install "spacy>=3.8,<3.9" nltk ipykernel
```

Install the spaCy model with `python -m spacy download en_core_web_sm`. The notebook retrieves two NLTK resources on first use.
