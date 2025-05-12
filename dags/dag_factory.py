import os, yaml
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'test',
    'depends_on_past': False,
    'start_date': datetime(2025, 5, 12),
    'retries': 0,
}

with DAG(
    dag_id='hello_world_bash_v1',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['example', 'bash'],
) as dag:

    run_script = BashOperator(
        task_id = "run_legacy_bash_script",
        bash_command = "$/legacy/bash/hello1.sh ",
    )

    run_script
