from datetime import timedelta


DEFAULT_ARGS = {
    "owner": "airflow",
    "email": ["airflow@example.com"],
    "email_on_failure": True,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}
RAW_DATA = "data/raw/{{ ds }}"
PROC_DATA = "data/processed/{{ ds }}"
MODEL_PATH = "data/models/{{ ds }}"
PRED_DATA = "data/predictions/{{ ds }}"
LOCAL_DATA = "/home/cyrus_arch/Рабочий стол/made/cyrusmsk/airflow_ml_dags/dags/"