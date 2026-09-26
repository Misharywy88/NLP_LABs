# Lab 4 - Classification and Evaluation

[Open the completed notebook](Lab%204.ipynb).

## Tasks

Five preprocessing steps; stratified train/test split; TF-IDF; Multinomial Naive Bayes; classification metrics; printed and plotted confusion matrix.

The notebook is a standalone solution to the assigned tasks in the instructor's handout, with short explanations and saved outputs. It uses the dataset specified for this lab. Teaching demonstrations from the handout are not duplicated.

## Run

Follow the [repository setup instructions](../README.md), open `Lab 4.ipynb`, and run all cells from top to bottom. See [data/README.md](data/README.md) for the source and local dataset details.

## Results

Results: 80.85% accuracy and 0.5493 macro-F1 on 30,455 held-out reviews. Neutral recall is only 0.22%; the notebook discusses this limitation. All 413,840 source rows are loaded before the documented filtering steps.
