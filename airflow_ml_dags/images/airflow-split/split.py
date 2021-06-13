import os

import click
import pandas as pd
from sklearn.model_selection import train_test_split


@click.command("split")
@click.option("--input-dir")
@click.option("--output-dir")
def split_data(input_dir: str, output_dir: str):
    data = pd.read_csv(os.path.join(input_dir, "data.csv"), index_col=0)
    target = pd.read_csv(os.path.join(input_dir, "target.csv"), index_col=0)
    X_train, X_test, y_train, y_test = train_test_split(
    data, target, test_size=0.5, random_state=1337)

    os.makedirs(output_dir, exist_ok=True)
    X_train.to_csv(os.path.join(output_dir, "X_train.csv"))
    X_test.to_csv(os.path.join(output_dir, "X_test.csv"))
    y_train.to_csv(os.path.join(output_dir, "y_train.csv"))
    y_test.to_csv(os.path.join(output_dir, "y_test.csv"))


if __name__ == '__main__':
    split_data()