import pickle
import os

import numpy as np
import pandas as pd
import click
from sklearn import datasets


@click.command("predict_model")
@click.option("--input-dir")
@click.option("--output-dir")
@click.option("--model-dir")
def predict_model(input_dir: str, output_dir: str, model_dir: str):
    digits = datasets.load_digits()
    with open(os.path.join(model_dir, "model.pkl"), "rb") as input_file:
        model = pickle.load(input_file)

    predicted = model.predict(digits.data)
    os.makedirs(output_dir, exist_ok=True)
    np.savetxt(os.path.join(output_dir, "prediction.csv"), predicted)


if __name__ == '__main__':
    predict_model()