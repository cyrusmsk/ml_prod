from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.filesystem import FileSensor
from airflow.utils.dates import days_ago

from vars import (
    DEFAULT_ARGS,
    RAW_DATA,
    PROC_DATA,
    LOCAL_DATA,
    MODEL_PATH,
)


with DAG(
    "train_process",
    default_args=DEFAULT_ARGS,
    schedule_interval="@weekly",
    start_date=days_ago(1),
    tags=["train_process"],
) as dag:

    data_sensor = FileSensor(
        task_id="data_sensor",
        filepath=f"{RAW_DATA}/data.csv",
        poke_interval=10,
        retries=10,
        mode="reschedule",
    )

    target_sensor = FileSensor(
        task_id="target_sensor",
        filepath=f"{RAW_DATA}/target.csv",
        poke_interval=10,
        retries=10,
        mode="reschedule",
    )

    preprocess_data = DockerOperator(
        image="airflow-preprocess",
        command=f"--input-dir={RAW_DATA} "
                f"--output-dir={PROC_DATA} "
        network_mode="bridge",
        task_id="preprocess_data",
        do_xcom_push=False,
        volumes=[f"{LOCAL_DATA}/:/data"],
    )

    split_data = DockerOperator(
        image="airflow-split",
        command=f"--input-dir={PROC_DATA} "
                f"--output-dir={PROC_DATA}",
        network_mode="bridge",
        task_id="split_data",
        do_xcom_push=False,
        volumes=[f"{LOCAL_DATA}/:/data"],
    )

    train_model = DockerOperator(
        image="airflow-train",
        command=f"--input-dir={PROC_DATA} "
                f"--model-dir={MODEL_PATH}",
        network_mode="bridge",
        task_id="train_model",
        do_xcom_push=False,
        volumes=[f"{LOCAL_DATA}/:/data"],
    )

    validate_model = DockerOperator(
        image="airflow-validate",
        command=f"--input-dir={PROC_DATA} "
                f"--model-dir={MODEL_PATH}",
        network_mode="bridge",
        task_id="validate_model",
        do_xcom_push=False,
        volumes=[f"{LOCAL_DATA}/:/data"],
    )

    [data_sensor, target_sensor] >> preprocess_data >> split_data >> train_model >> validate_model