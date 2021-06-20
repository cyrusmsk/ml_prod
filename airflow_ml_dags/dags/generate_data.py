from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago


from vars import DEFAULT_ARGS, RAW_DATA, LOCAL_DATA


with DAG(
    "generate_data",
    default_args=DEFAULT_ARGS,
    schedule_interval="@daily",
    start_date=days_ago(1),
    tags=["data_generation"],
) as dag:
    download_data = DockerOperator(
        image="airflow-generate-data",
        command=f"{RAW_DATA}",
        network_mode="bridge",
        task_id="docker-airflow-generate-data",
        do_xcom_push=False,
        volumes=[f"{LOCAL_DATA}:/data"],
    )