from datetime import datetime, timedelta
from airflow import DAG
import uuid
# from airflow.operators.python_operator import PythonOperator
import requests
import json
default_args = {
    'owner': 'Haiden',
    'start_date': datetime(2025, 10, 16, 17, 0),
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
    res= get_data()
    res= format_data(res)
    print(json.dumps(res, indent=3))
    return res


stream_data()













# with DAG('kafka_streaming_pipeline', default_args=default_args, schedule_interval='@daily', catchup=False) as dag: 
#     streaming_task = PythonOperator(
#         task_id='stream_data_from_api',
#         python_callable= stream_data 
#         )