import paho.mqtt.client as mqtt 
import random 
import time

CLIENT_NAME = "DummyGenerator"
MQTT_BROKER = "10.7.2.88"
TOPIC_1     = "HZHF/Lokatie1/Moisture"
TOPIC_2     = "HZHF/Lokatie1/Klepstand"


client = mqtt.Client(CLIENT_NAME)
client.connect(MQTT_BROKER)

while True:
    client.publish(TOPIC_1,  random.uniform(10, 80) )
    client.publish(TOPIC_2,  random.choice(("Open", "Dicht")) )
    time.sleep(1)
    
