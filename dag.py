from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import pandas as pd
import requests
import pytz

default_args = {
    'owner': 'usman',
    'start_date': days_ago(0),
    'email': ['usman.khan9805@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'usman',
    default_args=default_args,
    description='usmans Dag',
    schedule_interval='*/2 * * * *',  # run schedule after every 2 mins
)

def extract_data(**kwargs):
    url = "http://api.exchangeratesapi.io/v1/latest?base=EUR&access_key=e552f27977ecb70f1a9187ad666bc32b"
    response = requests.get(url)
    data = response.json()
    # Constructing a DataFrame with 'Currency' as index and 'Rate' as the value
    df = pd.DataFrame({'Currency': list(data['rates'].keys()), 'Rate': list(data['rates'].values())})
    kwargs['ti'].xcom_push(key='df2', value=df)

def load_data(**kwargs):
    df2 = kwargs['ti'].xcom_pull(task_ids='extract', key='df2')
    excel_file_path = '/home/usman/airflow/dags/excel_output.xlsx'
    df2.to_excel(excel_file_path, index=True)
    return excel_file_path

extract = PythonOperator(
    task_id='extract',
    python_callable=extract_data,
    provide_context=True,
    dag=dag,
)

load = PythonOperator(
    task_id='load',
    python_callable=load_data,
    provide_context=True,
    dag=dag,
)

extract >> load
