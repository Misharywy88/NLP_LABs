# Natural Language Processing Labs

Course lab notebooks, datasets, and brief explanations.

| Lab | Topic | Status |
| --- | --- | --- |
| [Lab 1](Lab%201/) | Introduction to NLP and SMS dataset exploration | Completed |
| [Lab 2](Lab%202/) | Text Preprocessing and Regular Expressions | Completed |
| [Lab 3](Lab%203/) | N-Gram Language Models | Completed |
| [Lab 4](Lab%204/) | Classification and Evaluation | Completed |
| [Lab 5](Lab%205/) | Text Representation | Completed |

## Run locally

Use Python 3.12. From the repository folder on Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m spacy download en_core_web_sm
.\.venv\Scripts\python.exe setup_nlp.py
.\.venv\Scripts\python.exe download_data.py
.\.venv\Scripts\python.exe -m jupyterlab
```

Open any completed lab notebook (for example, `Lab 2/Lab 2.ipynb`) and select **Run > Run All Cells**. In VS Code, select the `.venv` Python interpreter as the notebook kernel.

Lab 1 includes its dataset and saved outputs. After installing the dependencies, it runs without a download or account. Dataset attribution and source notes are included in `Lab 1/data/README.md`.

## Datasets and reproducibility

Labs 2-5 use the datasets specified in their assignments. The download script fetches missing files from Kaggle without overwriting existing files. The tweet datasets for Labs 2 and 3 and the Simpsons dataset for Lab 5 are stored locally and excluded from Git; their source license labels do not clearly permit redistribution. Lab 4 includes its full CC0 dataset compressed as gzip. Each lab's data README records its source and SHA-256 hash.

First-time setup requires internet access. Later notebook runs use the downloaded data, installed spaCy model, and local NLTK resources. Model splits and text generation use fixed random seeds. Saved notebook outputs allow the results to be reviewed on GitHub without rerunning.

Lab 5 trains a Skip-gram Word2Vec model with Gensim. It uses all nonempty spoken lines from the assigned Simpsons CSV, with a fixed seed and one worker. Saved outputs include all required character queries.
