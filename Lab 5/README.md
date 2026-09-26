# Lab 5 - Text Representation

[Open Lab 5.ipynb](Lab%205.ipynb).

## Completed tasks

1. TF-IDF cosine similarity for the four assigned sentences.
2. TF-IDF weights and important terms for the three assigned sentences.
3. Preprocess the Simpsons `spoken_words` column and train Skip-gram Word2Vec.
4. Find words similar to `homer`, `marge`, and `bart`.
5. Find the odd word out in all three specified groups.

## Dataset check

The Simpsons dataset is explicitly required by Tasks 3-5. It is not merely a sample. The fake/real news dataset is used only in the handout's demonstration. The missing CSV and download source have been supplied; no additional task input is needed.

## Run

Follow the [repository setup instructions](../README.md), then run every cell in order. The notebook includes saved outputs. Word2Vec trains locally with a fixed seed and one worker; training may take a few minutes. The required Gensim dependency is included in `requirements.txt`.

See [data/README.md](data/README.md) for provenance and download details. The dataset is stored locally but excluded from Git; the download script retrieves it after cloning.

## Results

All five tasks ran successfully. The Word2Vec model uses 132,096 tokenized spoken lines and a 44,324-token vocabulary. The odd-one-out results are `milhouse`, `nelson`, and `homer`, in the order of the assigned groups. Detailed matrices, term rankings, and word similarities are saved in the notebook.
