import os
from typing import List

from py._path.local import LocalPath

from heart_ml.models.predict_model import predict_pipeline
from heart_ml.entities import (
    PredictPipelineParams,
    FeatureParams,
)


def test_predict_e2e(
    tmpdir: LocalPath,
    dataset_path: str,
    out_dataset_path: str,
    categorical_features: List[str],
    numerical_features: List[str],
    target_col: str,
    features_to_drop: List[str],
):
    tmp_output_model_path = tmpdir.join("model.pkl")
    tmp_metric_path = tmpdir.join("metrics.json")
    params = PredictPipelineParams(
        input_data_path=dataset_path,
        output_data_path=out_dataset_path,
        output_model_path=tmp_output_model_path,
        metric_path=tmp_metric_path,
        feature_params=FeatureParams(
            numerical_features=numerical_features,
            categorical_features=categorical_features,
            target_col=target_col,
            features_to_drop=features_to_drop,
        ),
    )
    expected_output_path = predict_pipeline(params)
    assert expected_output_path == out_dataset_path
    assert os.path.exists(expected_output_path)