import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time

MQTT_BROKER = "localhost"

client = mqtt.Client("Pubisher")
client.connect( MQTT_BROKER )

def measureTemperature():
    return uniform(20.0, 21.0)

while True:
    temperature = measureTemperature()
    client.publish("DZHF/ARJAN2/TEMPERATURE", temperature)
    client.publish("DZHF/WES2/TEMPERATURE", temperature)
    print("Just published to topic TEMPERATURE :", temperature)
    time.sleep(2)
    
