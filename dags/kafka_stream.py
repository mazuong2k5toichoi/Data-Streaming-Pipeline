from datetime import datetime, timedelta
from airflow import DAG
import uuid
from airflow.operators.python_operator import PythonOperator
import requests
import json
from kafka import KafkaProducer
import time
import logging
default_args = {
    'owner': 'Haiden',
    'start_date': datetime(2023, 10, 15, 17, 0),
}
def get_data():

    res = requests.get('https://randomuser.me/api/')
    res = res.json()['results'][0]
    return res

def format_data(res):
    data = {}
    location = res['location']
    # data['id'] = uuid.uuid4()
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data

def stream_data():


    curr_time = time.time()
    producer = KafkaProducer(bootstrap_servers = ['broker:29092'], max_block_ms=5000)

    while True:
        if time.time() > curr_time + 60:
            break
        try:
            res = get_data()
            res = format_data(res)

            producer.send('users_created', json.dumps(res).encode('utf-8'))
            logging.info(f"Data sent: {res}")

        except Exception as e:
            logging.error(f"An error occured: {e}")
            continue

with DAG('kafka_streaming_pipeline', default_args=default_args, schedule_interval='@daily', catchup=False) as dag: 
    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable= stream_data 
        )