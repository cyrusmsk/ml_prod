import os
import pickle

import click
import pandas as pd

import numpy as np
from sklearn import metrics


@click.command("validate")
@click.option("--input-dir")
@click.option("--model-dir")
def validate_model(input_dir: str, model_dir: str):
    # Load data and model
    X_test = pd.read_csv(os.path.join(input_dir, "X_test.csv"), index_col=0)
    y_test = pd.read_csv(os.path.join(input_dir, "y_test.csv"), index_col=0)

    with open(os.path.join(model_dir, "model.pkl"), "rb") as input_file:
        model = pickle.load(input_file)

    y_pred = model.predict(X_test)
    matrix = metrics.confusion_matrix(y_pred, y_test)
    
    os.makedirs(model_dir, exist_ok=True)
    with open(os.path.join(model_dir, "matrix.csv"), 'w') as output_file:
        output_file.write(np.array2string(matrix, separator=', '))


if __name__ == '__main__':
    validate_model()