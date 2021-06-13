import os
import pickle

import click
import pandas as pd
import numpy as np
from sklearn import metrics


@click.command("validate")
@click.option("--input-dir")
@click.option("--model-dir")
def validate_model(data_dir: str, model_dir: str):
    # Load data and model
    X_test = pd.read_csv(os.path.join(data_dir, "X_test.csv"), index_col=0)
    y_test = pd.read_csv(os.path.join(data_dir, "y_test.csv"), index_col=0)

    with open(os.path.join(model_dir, "model.pkl"), "rb") as input_file:
        model = pickle.load(input_file)

    disp = metrics.plot_confusion_matrix(clf, X_test, y_test)
    # Save metrics to local filesystem
    
    os.makedirs(model_dir, exist_ok=True)
    with open(os.path.join(model_dir, "matrix.csv"), 'w') as output_file:
        output_file.write(np.array2string(disp.confusion_matrix, separator=', '))


if __name__ == '__main__':
    validate_model()