import os

import pytest
from typing import List


@pytest.fixture()
def tmpdir():
    curdir = os.path.dirname(__file__)
    return os.path.join(curdir, "tmp_data")


@pytest.fixture()
def dataset_path():
    curdir = os.path.dirname(__file__)
    return os.path.join(curdir, "tmp_data/train_data_sample.csv")


@pytest.fixture()
def out_path():
    curdir = os.path.dirname(__file__)
    return os.path.join(curdir, "tmp_data/out.csv")


@pytest.fixture()
def out_dataset_path():
    curdir = os.path.dirname(__file__)
    return os.path.join(curdir, "tmp_data/out_data.csv")


@pytest.fixture()
def target_col():
    return "target"


@pytest.fixture()
def categorical_features() -> List[str]:
    return [
        "ca",
        "cp",
        "exang",
        "fbs",
        "restecg",
        "sex",
        "slope",
        "thal",
    ]


@pytest.fixture
def numerical_features() -> List[str]:
    return [
        "age",
        "chol",
        "oldpeak",
        "thalach",
        "trestbps",
    ]


@pytest.fixture()
def features_to_drop() -> List[str]:
    return []
