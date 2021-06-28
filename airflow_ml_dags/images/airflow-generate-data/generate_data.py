import os
import click
import pandas as pd
from sklearn.datasets import load_digits


@click.command("generate_data")
@click.argument("output_dir")
def generate_data(output_dir: str):
    digits = load_digits()
    os.makedirs(output_dir, exist_ok=True)
    pd.DataFrame(digits.data).to_csv(os.path.join(output_dir, "data.csv"))
    pd.DataFrame(digits.target).to_csv(os.path.join(output_dir, "target.csv"))


if __name__ == '__main__':
    generate_data()