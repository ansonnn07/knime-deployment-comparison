"""
Testing pypmml module, still getting unknown errors when making predictions.
"""

import os

import numpy as np
import pandas as pd
import time
from sklearn.preprocessing import OrdinalEncoder

from sklearn2pmml import sklearn2pmml
from pypmml import Model

TRAIN_CSV = os.path.join("data", "ChurnPrediction_TrainingSet.xlsx")
TEST_CSV = os.path.join("data", "ChurnPrediction_TestSet.xlsx")

train_df = pd.read_excel(TRAIN_CSV)
test_df = pd.read_excel(TEST_CSV)

# prepare the training and test set
X_train1 = train_df.drop(columns=["Churn", "Phone"])
y_train1 = train_df["Churn"].copy()

X_test1 = test_df.drop(columns=["Churn", "Phone"])
y_test1 = test_df["Churn"].copy()

# change the nominal columns into encoded numbers
encoder = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)
X_train1[["State"]] = encoder.fit_transform(X_train1[["State"]]).astype(int)
X_test1[["State"]] = encoder.transform(X_test1[["State"]]).astype(int)

# load the model
knime_model = Model.load("models/knime_decision_tree.pmml")

# check the model config
print(f"{dir(knime_model) = }\n")

print(f"{X_train1.columns = }\n")
print(f"{len(X_train1.columns) = }\n")

print(f"{knime_model.inputNames = }\n")
print(f"{len(knime_model.inputNames) = }\n")

print("[INFO] Input columns of DataFrame same with model input names? : ", end="")
print(f"{X_train1.columns.tolist() ==  knime_model.inputNames}")

print(f"{knime_model.targetNames = }\n")

# print(f"[INFO] Making predictions ...")
# start_time = time.perf_counter()
# y_preds = knime_model.predict(X_train1)
# end_time = time.perf_counter()
# total_time = end_time - start_time
# print(f"[INFO] Total time elapsed: {total_time:.2f} s")
