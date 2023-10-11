""" paho moet met PIP geinstalleerd worden
    Dit programma is gemaakt door Arjan
    Versiedatu, 6-2-2023
"""
import paho.mqtt.client as mqtt 
from random import uniform
import time

CLIENT_NAME = "gerbdbr"
MQTT_BROKER = "10.9.41.92"
PIN_LED = 3 # op pin 3 is de led aangesloten
TOPIC_TEMP = "DZHF/temp/Arjan"

client = mqtt.Client(CLIENT_NAME)
client.connect(MQTT_BROKER)

def measure_temperature():
   return uniform(40.0, 60.0)

while True:
    temperature = measure_temperature()
    client.publish(TOPIC_TEMP, temperature)
    print("Just published to topic TEMPERATURE :", temperature)
    time.sleep(2)
    
