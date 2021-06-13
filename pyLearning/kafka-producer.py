from kafka import KafkaProducer
from json import dumps,loads
import requests
import time
"""
from datetime import datetime


import random
from restcountries import RestCountryApiV2 as rapi

"""

TOPIC_NAME_CONS="mytopic"
BOOTSTRAP_SERVERS_CONS='localhost:9092'
RANDOM_USER_API_URL="https://randomuser.me/api/0.8"

if __name__=="__main__":
    print("Producer from Pycharm app")

    kafka_producer_obj=None
    kafka_producer_obj=KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS_CONS, value_serializer=lambda x: dumps(x).encode('utf-8'))

    event_server_statu_color_name_list=["Red|Severity 1","Orange|Severity 2"]
    event_server_type_list=["Application Server","Client Servers"]

    message = "Hello from pycharm2"

    while True:
        response_data= requests.get(url=RANDOM_USER_API_URL)
        data_to_send= response_data.json()
        data=dumps(data_to_send)
        kafka_producer_obj.send(TOPIC_NAME_CONS,data)
        time.sleep(2)
    #data2="{\"results\": [{\"user\": {\"gender\": \"female\", \"name\": {\"title\": \"mrs\", \"first\": \"zoe\", \"last\": \"webb\"}, \"location\": {\"street\": \"5791 tara street\", \"city\": \"ballybofey-stranorlar\", \"state\": \"hawaii\", \"zip\": 98238}, \"email\": \"zoe.webb@example.com\", \"username\": \"silverfish872\", \"password\": \"brewster\", \"salt\": \"8l65BU9p\", \"md5\": \"31aac55d0b915238b38efd40cc7be1b1\", \"sha1\": \"64ea5a6026d09ced6e66525f90bbd62e94166a21\", \"sha256\": \"822f37972107f09baefd8204e522c6d9e0053fb00548c56a0528c7abe7110dab\", \"registered\": 1181216184, \"dob\": 852510605, \"phone\": \"021-652-0429\", \"cell\": \"081-242-3680\", \"PPS\": \"7325789T\", \"picture\": {\"large\": \"https://randomuser.me/api/portraits/women/7.jpg\", \"medium\": \"https://randomuser.me/api/portraits/med/women/7.jpg\", \"thumbnail\": \"https://randomuser.me/api/portraits/thumb/women/7.jpg\"}}}], \"nationality\": \"IE\", \"seed\": \"28b0f72bfc3a550409\", \"version\": \"0.8\"}"
    #print(loads(data2))


    """

    def foo(name):
        country_list = rapi.get_countries_by_name("India")
        return country_list

    country=foo("France")
    print(country)
    """