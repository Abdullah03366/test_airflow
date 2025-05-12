import os, yaml
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

DEFAULT_ARGS = {
    'owner': 'test',
    'start_date': datetime(2025, 5, 12),
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
    'depends_on_past': False,
}

BASE_SCRIPT_PATH = '/opt/airflow/dags/legacy/bash'
CONFIG_FILE     = '/opt/airflow/dags/dags/jobs_config.yml'

with open(CONFIG_FILE) as f:
    jobs = yaml.safe_load(f)

for job in jobs:
    dag_id = f"test.legacy.bash.{job['job_id']}_v1"
    dag = DAG(
        dag_id=dag_id,
        default_args=DEFAULT_ARGS,
        schedule_interval='@daily',
        catchup=False,
        tags=['legacy','bash']
    )
    BashOperator(
        task_id=f"run_{job['job_id']}",
        bash_command=f"bash {BASE_SCRIPT_PATH}/{job['script']}",
        dag=dag,
        do_xcom_push=False,
    )
    globals()[dag_id] = dag
