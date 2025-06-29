from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

with DAG(
    dag_id='compact_python_workflow',
    start_date=datetime(2025, 6, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    t1 = PythonOperator(task_id='stap_1', python_callable=lambda: print("Stap 1: Data ophalen"))
    t2 = PythonOperator(task_id='stap_2', python_callable=lambda: print("Stap 2: Bewerken"))
    t3 = PythonOperator(task_id='stap_3', python_callable=lambda: print("Stap 3: Valideren"))
    t4 = PythonOperator(task_id='stap_4', python_callable=lambda: print("Stap 4: Opslaan"))

    t1 >> t2 >> t3 >> t4