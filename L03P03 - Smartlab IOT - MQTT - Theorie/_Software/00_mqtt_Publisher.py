import paho.mqtt.client as mqtt 
from random import uniform
import time

CLIENT_NAME = "Inside"
MQTT_BROKER = "192.168.1.99"

client = mqtt.Client(CLIENT_NAME)
client.connect(MQTT_BROKER)


def measure_temperature():
    return uniform(20.0, 21.0)


while True:
    temperature = measure_temperature()
    client.publish("TEMPERATURE", temperature)
    print("Just published to topic TEMPERATURE :", temperature)
    time.sleep(2)
    
