import paho.mqtt.client as mqtt 
from random import uniform
import time

CLIENT_NAME = "Inside"
SSID           = "MQTT_WIFI"
SSID_PASSWORD  = "kambergArjan"

MQTT_BROKER    = "192.168.1.99"

client = mqtt.Client(CLIENT_NAME)
client.connect(MQTT_BROKER)

while True:
    client.publish("DZHF/TEMPERATURE/Sensor 1",  uniform(15.0, 23.0) )
    client.publish("DZHF/TEMPERATURE/Sensor 2",  uniform(15.0, 23.0) )
    client.publish("DZHF/TEMPERATURE/Sensor 3",  uniform(15.0, 23.0) )
    client.publish("DZHF/TEMPERATURE/Sensor 4",  uniform(15.0, 23.0) )
    client.publish("DZHF/TEMPERATURE/Sensor 5",  uniform(15.0, 23.0) )
    client.publish("DZHF/TEMPERATURE/Sensor 6",  uniform(15.0, 23.0) )
    client.publish("DZHF/TEMPERATURE/Sensor 7",  uniform(15.0, 23.0) )
    
    client.publish("Nederland/LUCHTVOCHTIGHEID/Sensor 1",  uniform(0, 100) )
    client.publish("Belgie/LUCHTVOCHTIGHEID/Sensor 2",  uniform(0, 100) )
    client.publish("Duitsland/LUCHTVOCHTIGHEID/Sensor 3",  uniform(0, 100) )
    client.publish("Frankrijk/LUCHTVOCHTIGHEID/Sensor 4",  uniform(0, 100) )
    client.publish("Engeland/LUCHTVOCHTIGHEID/Sensor 5",  uniform(0, 100) ) 
   

    client.publish("Nederland/PRESSURE/Sensor 1",  uniform(900, 1100) )
    client.publish("Belgie/PRESSURE/Sensor 2",  uniform(0.9, 1.1) )
    client.publish("Duitsland/PRESSURE/Sensor 3",  uniform(0.9, 1.1) )
    client.publish("Frankrijk/PRESSURE/Sensor 4",  uniform(0.9, 1.1) )
    client.publish("Engeland/PRESSURE/Sensor 5",  uniform(0.9, 1.1) ) 
    
    print("Published")
    time.sleep(1)
    
