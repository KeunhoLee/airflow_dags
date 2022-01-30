from airflow import DAG
from airflow.operators.bash_operator import BashOperator

from datetime import datetime

with DAG(
    "test_scheduler",
    start_date=datetime(2021, 12, 24),
    schedule_interval="50 1 * * 0,1,2,3,4",
    catchup=True
) as dag:

    echo_hello = BashOperator(
        task_id="echo_hello",
        bash_command="echo 'hello'",
        do_xcom_push=False
    )

    touch_hello = BashOperator(
        task_id="touch_hello",
        bash_command="touch ~/hello",
        do_xcom_push=False
    )

    echo_hello, touch_hello

