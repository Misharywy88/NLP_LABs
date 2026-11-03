# Lab 10 — English–French machine translation

Run the supplied three-pair LSTM example, explain its layers, then translate product listings, reviews, and store policies with a pretrained Marian model. The evaluation reports mean sentence chrF (0–1) against one French reference per example. Different valid wording can reduce this score.

## Run the notebook

Open this folder in VS Code with the Python and Jupyter extensions. Use a Python 3.12 kernel. Install the dependencies in that environment, then open `Lab10_Completed.ipynb` and choose **Run All**.

```shell
python -m pip install tensorflow scikit-learn torch "transformers==4.57.3" sentencepiece sacremoses pandas nltk ipykernel ipywidgets
```

The bundled CSV contains 60 sentence pairs randomly sampled (seed 42) from rows matching shopping-related English words in the [assigned Kaggle dataset](https://www.kaggle.com/datasets/devicharith/language-translation-englishfrench). It is an evaluation sample. The first run downloads the pretrained English–French translator.
