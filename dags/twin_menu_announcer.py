from airflow import DAG
from airflow.operators.bash_operator import BashOperator

import pendulum
from datetime import datetime

#local_tz = pendulum.timezone("Asia/Seoul")

with DAG(
    "twin_menu_announcer",
    start_date=datetime(2021, 12, 24),
    schedule_interval="30 1 * * 1,2,3,4,5",
    catchup=True
) as dag:

    scrap_west_menu = BashOperator(
        task_id="scrap_west_menu",
        bash_command="cd /home/keunholee/scrap_twin_menu && pipenv run python -m scrap_twin_menu main west",
        do_xcom_push=False
    )

    scrap_east_menu = BashOperator(
        task_id="scrap_east_menu",
        bash_command="cd /home/keunholee/scrap_twin_menu && pipenv run python -m scrap_twin_menu main east",
        do_xcom_push=False
    )

    send_west_menu = BashOperator(
        task_id="send_west_menu",
        bash_command="cd /home/keunholee/scrap_twin_menu && pipenv run python -m send_menu main west",
        do_xcom_push=False
    )

    send_east_menu = BashOperator(
        task_id="send_east_menu",
        bash_command="cd /home/keunholee/scrap_twin_menu && pipenv run python -m send_menu main east",
        do_xcom_push=False
    )

    scrap_west_menu >> scrap_east_menu >> send_west_menu >> send_east_menu

