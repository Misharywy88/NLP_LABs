# Lab 6 — Yelp Sentiment Classification

This lab compares two ways to classify restaurant reviews as negative (0) or positive (1). Both models use the same 800 training reviews and 200 test reviews from the supplied Yelp dataset.

## Files

- `Lab6_Completed.ipynb` contains the completed exercises and saved results.
- `dataset/07-yelp-dataset.txt` contains the 1,000 original reviews and their sentiment labels.

## Run in VS Code

1. Open the **Lab 6** folder in VS Code and enable the Python and Jupyter extensions.
2. Open a terminal in this folder. To install the libraries in your chosen Python environment, run:

   ```sh
   python -m pip install pandas numpy scikit-learn torch gensim ipykernel
   ```

3. Open the notebook, choose **Select Kernel**, and select the same Python environment.
4. Choose **Run All**. Keep the dataset in its supplied subfolder so the notebook can find it.

## Recorded results

| Model | Correct predictions | Test accuracy |
| --- | ---: | ---: |
| TF-IDF neural network | 151 of 200 | 75.5% |
| Word2Vec neural network | 100 of 200 | 50.0% |

The Word2Vec model averages the known word vectors in each review and feeds the result into three hidden layers of 128, 64, and 32 neurons. After 15 epochs, it predicted 196 reviews as negative and four as positive. The test set contained 100 reviews of each class.
