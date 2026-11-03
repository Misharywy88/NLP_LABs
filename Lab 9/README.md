# Lab 9 — Named entity recognition

Inspect pretrained predictions, annotate an agreement, count people and organizations, then train a custom recognizer for 20 iterations. The single training sentence demonstrates the workflow and cannot establish generalization.

## Run the notebook

Open this folder in VS Code with the Python and Jupyter extensions. Use a Python 3.12 kernel. Install the dependencies in that environment, then open `Lab9_Completed.ipynb` and choose **Run All**.

```shell
python -m pip install "spacy>=3.8,<3.9" ipykernel
```

Install the pretrained model with `python -m spacy download en_core_web_sm`. Task 1 prompts for a sentence. Task 3 writes and reloads the included `custom_ner_model/` directory.

The saved interactive example uses “Steve Jobs worked at Apple in California.” The corrected agreement contains one person and two organizations. In the new test sentence, the custom model recognizes Bill Gates but misses Microsoft.
