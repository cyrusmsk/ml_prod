import pickle
from typing import Dict, Union

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from catboost import CatBoostClassifier

from heart_ml.entities.train_params import TrainingParams
from heart_ml.entities.feature_params import FeatureParams

ClassifierModel = Union[RandomForestClassifier, CatBoostClassifier]


def train_model(
    features: pd.DataFrame, target: pd.Series, train_params: TrainingParams
) -> ClassifierModel:
    if train_params.model_type == "CatBoostClassifier":
        model = CatBoostClassifier(
            random_seed=train_params.random_state
        )
    elif train_params.model_type == "RandomForestClassifier":
        model = RandomForestClassifier(
            random_state=train_params.random_state
        )
    else:
        raise NotImplementedError()
    model.fit(features, target)
    return model


def predict_model(
    model: ClassifierModel, features: pd.DataFrame
) -> np.ndarray:
    predicts = model.predict(features)
    return predicts


def evaluate_model(
    predicts: np.ndarray, target: pd.Series
) -> Dict[str, float]:
    return {
        "r2_score": r2_score(target, predicts),
        "rmse": mean_squared_error(target, predicts, squared=False),
        "mae": mean_absolute_error(target, predicts),
    }


def serialize_model(model: ClassifierModel, output: str) -> str:
    with open(output, "wb") as f:
        pickle.dump(model, f)
    return output


def deserialize_model(input_path: str) -> ClassifierModel:
    with open(input_path, "rb") as f:
        result = pickle.load(f)
    return result