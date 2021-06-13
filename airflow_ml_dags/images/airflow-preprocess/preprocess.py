import os
import pickle

import click
import pandas as pd


@click.command("preprocess")
@click.option("--input-dir")
@click.option("--output-dir")
def preprocess(input_dir: str, output_dir: str):
    features = pd.read_csv(os.path.join(input_dir, "data.csv"), index_col=0)
    target = pd.read_csv(os.path.join(input_dir, "target.csv"), index_col=0)
    #n_samples = len(features)
    #data = features.reshape((n_samples, -1))
    os.makedirs(output_dir, exist_ok=True)
    features.to_csv(os.path.join(output_dir, "data.csv"))
    target.to_csv(os.path.join(output_dir, "target.csv"))
    

if __name__ == '__main__':
    preprocess()