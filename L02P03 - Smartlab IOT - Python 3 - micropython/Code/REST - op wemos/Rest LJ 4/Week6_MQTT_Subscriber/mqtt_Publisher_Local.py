import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time

#MQTT_BROKER ="192.168.2.128" #mqtt.eclipseprojects.io
#MQTT_BROKER ="localhost"
MQTT_BROKER ="mqtt.eclipseprojects.io"
MQTT_BROKER = "test.mosquitto.org"

client = mqtt.Client("Pubisher")
client.username_pw_set(username="mqtt", password="Test4321")
client.connect( MQTT_BROKER ) 

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to topic TEMPERATURE")
    time.sleep(2)
    
