from datetime import datetime

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
    access_control={
        "example_viewer": {"can_read"},
    },
) as dag:

    hello_bash = BashOperator(
        task_id='hello_world_task',
        bash_command='echo "Hello, World!"',
    )

    hello_bash
