import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

SLEEP = 2
MQTT_PUBLISHER = "Publisher"
#MQTT_BROKER = "localhost"
#MQTT_BROKER = "test.mosquitto.org"
MQTT_BROKER = "10.7.2.109"
MQTT_TOPIC = "DZHF/ARJAN/TEMPERATURE"

client = mqtt.Client( MQTT_PUBLISHER )
client.connect( MQTT_BROKER )

def measureTemperature():
    return uniform(10.0,30.0)

while True:
    temp = measureTemperature()
    client.publish(MQTT_TOPIC, temp)
    print(temp)
    time.sleep( SLEEP )