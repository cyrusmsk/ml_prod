import os
import pickle

import click
import pandas as pd
from sklearn.svm import SVC


@click.command("train_model")
@click.option("--input-dir")
@click.option("--model-dir")
def train_model(input_dir: str, model_dir: str):
    model = SVC(gamma=0.001)
    X_train = pd.read_csv(os.path.join(input_dir, "X_train.csv"), index_col=0)
    y_train = pd.read_csv(os.path.join(input_dir, "y_train.csv"), index_col=0)
    model.fit(X_train, y_train)
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "model.pkl"), "wb") as output_file:
        pickle.dump(model, output_file)


if __name__ == '__main__':
    train_model()