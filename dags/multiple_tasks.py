from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='bash_data_pipeline_demo',
    start_date=datetime(2025, 6, 1),
    schedule_interval=None,
    catchup=False,
    tags=['demo', 'bash'],
) as dag:

    fetch_data = BashOperator(
        task_id='fetch_data_from_source',
        bash_command='echo "Stap 1: Ophalen van ruwe data uit externe bron..."'
    )

    process_data = BashOperator(
        task_id='process_and_clean_data',
        bash_command='echo "Stap 2: Bewerken en opschonen van data..."'
    )

    validate_data = BashOperator(
        task_id='validate_processed_data',
        bash_command='echo "Stap 3: Valideren van bewerkte data..."'
    )

    save_data = BashOperator(
        task_id='save_data_to_storage',
        bash_command='echo "Stap 4: Opslaan van gevalideerde data in storage..."'
    )

    fetch_data >> process_data >> validate_data >> save_data
