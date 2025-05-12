import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

SCRIPT_SUBDIR = "scripts"
SCRIPT_NAME = "hello1.sh"

DAG_FOLDER_TEMPLATE = '{{ dag_run.dag.folder }}' 

FULL_SCRIPT_PATH_TEMPLATE = os.path.join(DAG_FOLDER_TEMPLATE, SCRIPT_SUBDIR, SCRIPT_NAME)

default_args = {
    'owner': 'test',
    'depends_on_past': False,
    'start_date': datetime(2025, 5, 12),
    'retries': 0,
}

with DAG(
    dag_id='hello_world_legacy_bash_v2',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['example', 'bash', 'gitsync'],
) as dag:
    run_script = BashOperator(
        task_id="run_legacy_bash_script",
        bash_command=f"bash {FULL_SCRIPT_PATH_TEMPLATE}", 
    )
    
    run_script
