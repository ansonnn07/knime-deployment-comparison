# Comparison between KNIME and Python Machine Learning Models

A repo to show comparison between models exported from KNIME and Python.

Things to compare:
1. Train deep learning models using Keras in Python and export to KNIME.
2. Load the deep learning models exported from KNIME to evaluate the results in Python.
3. Repeat steps 1-2 for a conventional machine learning model (e.g. Decision Tree)
4. Compare the evaluation results done in Python and KNIME.

## Installation
TensorFlow library for loading and training of deep learning models. Refer to the YouTube video [here](https://youtu.be/hHWkvEcDBO0).

Using `sklearn-pmml-model` library from [here](https://github.com/iamDecode/sklearn-pmml-model), to load PMML model.
Follow the installation steps explained in the GitHub repo.

Using `sklearn2pmml` library from [here](https://github.com/jpmml/sklearn2pmml) to create PMML model.

## Comparison Results

![overall_comparison-dl-ml](results/overall_comparison-dl-ml.png)

You may refer to the `results` folder for each of the individual confusion matrix for different models.