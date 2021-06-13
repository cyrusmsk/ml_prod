from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.filesystem import FileSensor
from airflow.utils.dates import days_ago

from vars import (
    DEFAULT_ARGS,
    RAW_DATA,
    LOCAL_DATA,
    MODEL_PATH,
    PRED_DATA,
)


with DAG(
    "predict_pipeline",
    default_args=DEFAULT_ARGS,
    schedule_interval="@daily",
    start_date=days_ago(1),
    tags=["predict_process"],
) as dag:

    data_sensor = FileSensor(
        task_id="data_sensor",
        filepath=f"{RAW_DATA}/data.csv",
        poke_interval=10,
        retries=10,
        mode="reschedule",
    )

    model_sensor = FileSensor(
        task_id="model_sensor",
        filepath=f"{MODEL_PATH}/model.pkl",
        poke_interval=10,
        retries=10,
        mode="reschedule",
    )

    predict_model = DockerOperator(
        image="airflow-predict",
        command=f"--input-dir={RAW_DATA} "
                f"--output-dir={PRED_DATA} "
                f"--model-dir={MODEL_PATH}",
        network_mode="bridge",
        task_id="predict_model",
        do_xcom_push=False,
        volumes=[f"{LOCAL_DATA}/:/data"],
    )

    [data_sensor, model_sensor] >> predict_model