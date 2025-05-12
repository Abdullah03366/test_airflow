from airflow.operators.bash import BashOperator

hello_task = BashOperator(
    task_id='hello_world_bash',
    bash_command='echo "Hello, World!"',
)
