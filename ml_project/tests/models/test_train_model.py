import os
import pickle
from typing import List, Tuple

import pandas as pd
import pytest
from py._path.local import LocalPath
from catboost import CatBoostClassifier

from heart_ml.data.make_dataset import read_data
from heart_ml.entities import TrainingParams
from heart_ml.entities.feature_params import FeatureParams
from heart_ml.features.build_features import make_features, extract_target, build_transformer
from heart_ml.models.model_fit_predict import (
    train_model, 
    serialize_model,
    predict_model,
    deserialize_model
)


@pytest.fixture
def features_and_target(
    dataset_path: str, categorical_features: List[str], numerical_features: List[str]
) -> Tuple[pd.DataFrame, pd.Series]:
    params = FeatureParams(
        categorical_features=categorical_features,
        numerical_features=numerical_features,
        features_to_drop=[],
        target_col="target",
    )
    data = read_data(dataset_path)
    transformer = build_transformer(params)
    transformer.fit(data)
    features = make_features(transformer, data)
    target = extract_target(data, params)
    return features, target


def test_train_model(features_and_target: Tuple[pd.DataFrame, pd.Series]):
    features, target = features_and_target
    model = train_model(features, target, train_params=TrainingParams())
    assert isinstance(model, CatBoostClassifier)
    assert model.predict(features).shape[0] == target.shape[0]


def test_predict_model(features_and_target: Tuple[pd.DataFrame, pd.Series]):
    features, target = features_and_target
    model = train_model(features, target, train_params=TrainingParams())
    predicts = predict_model(model, features)
    assert predicts.shape > 10


def test_serialize_model(tmpdir: LocalPath):
    expected_output = tmpdir.join("model.pkl")
    n_estimators = 10
    model = CatboostClassifier(n_estimators=n_estimators)
    real_output = serialize_model(model, expected_output)
    assert real_output == expected_output
    assert os.path.exists


def test_evaluate_model(features_and_target: Tuple[pd.DataFrame, pd.Series]):
    features, target = features_and_target
    model = train_model(features, target, train_params=TrainingParams())
    predicts = predict_model(model, features)
    result_dict = evaluate_model(predicts, target)
    assert "r2_score" in result_dict.keys()
    assert "rmse" in result_dict.keys()
    assert "mae" in result_dict.keys()


def test_desirialize_model(tmpdir: LocalPath):
    expected_output = tmpdir.join("model.pkl")
    n_estimators = 10
    model = CatBoostClassifier(n_estimators=n_estimators)
    real_output = serialize_model(model, expected_output)
    model = deserialize_model(real_output)
    assert isinstance(model, CatBoostClassifier)