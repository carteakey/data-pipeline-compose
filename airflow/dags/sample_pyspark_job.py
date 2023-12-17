from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    # 'retries': 1,
    # 'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    "sample_run_pyspark",
    default_args=default_args,
    schedule_interval=None,  # "timedelta(days=1)",
    catchup=False,  # Prevents backfilling
)

t1 = BashOperator(
    task_id="sample_pyspark",
    bash_command="docker exec spark-master /spark/bin/spark-submit --master spark://spark-master:7077 /opt/scripts/pyspark/sample_pyspark.py",
    dag=dag,
)
