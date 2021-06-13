from kafka import KafkaConsumer
from json import loads
import time

bootstrap_servers = ['localhost:9092']
topicName = 'mytopic'
#KAFKA_GROUP_NAME = "console-consumer-24645"
KAFKA_GROUP_NAME = "myconsumer1"

if __name__ == "__main__":
    print("Kafka Consumer Application")
    #consumer = KafkaConsumer(topicName, group_id='console-consumer-24645', bootstrap_servers=bootstrap_servers,
                             #auto_offset_reset='earliest')
    #consumer = KafkaConsumer(topicName, group_id=KAFKA_GROUP_NAME, bootstrap_servers=bootstrap_servers,auto_offset_reset='earliest')
    consumer = KafkaConsumer(topicName,
                             group_id=KAFKA_GROUP_NAME + time.time(),
                             bootstrap_servers=bootstrap_servers,
                             auto_offset_reset='earliest',
                             enable_auto_commit=True,
                             value_deserializer = lambda x : loads(x.decode('utf-8')))


    for message in consumer:
        #print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
        print("%s:%d:%d: key=%s " % (message.topic, message.partition, message.offset, message.key))

    print("no data found")
