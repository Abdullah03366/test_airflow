from datetime import datetime

from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator

with DAG(
    dag_id="ssh_grep_example",
    start_date= datetime(2025, 5, 20),
    schedule_interval=None,
    catchup=False,
    tags=["example", "ssh"],
) as dag:
    run_grep = SSHOperator(
        task_id="run_grep",
        ssh_conn_id="ssh_grep",
        command="python3 /opt/ssh-grep/hello_grep.py",
    )

    run_grep
