# Lab 3 - N-Gram Language Models

[Open the completed notebook](Lab%203.ipynb).

## Tasks

Tweet preprocessing; bigram MLE training; held-out evaluation; generated text; P(is | pakistan); word and sentence perplexity.

The notebook is a standalone solution to the assigned tasks in the instructor's handout, with short explanations and saved outputs. It uses the dataset specified for this lab. Teaching demonstrations from the handout are not duplicated.

## Run

Follow the [repository setup instructions](../README.md), open `Lab 3.ipynb`, and run all cells from top to bottom. See [data/README.md](data/README.md) for the source and local dataset details.

## Results

The model uses 116,699 unique cleaned tweets with an 80/20 split. `P(is | pakistan)` is approximately 0.04269. Test perplexity is infinite because unseen bigrams have zero probability under unsmoothed MLE. The notebook explains the two interpretations of single-word perplexity and documents excluding 6,538 tweets with damaged text encoding.
