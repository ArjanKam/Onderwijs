import paho.mqtt.client as mqtt 
import random 
import time

CLIENT_NAME = "DummyGenerator"
MQTT_BROKER = "10.7.2.154"
COUNTRIES   = ("Nederland", "Belgie", "Duitsland", "Frankrijk", "Engeland" )
TEMPERATURE = "Temperature"
PRESSURE    = "Pressure"
HUMIDITY    = "Humidity"
SENSOR      = "Sensor"

client = mqtt.Client(CLIENT_NAME)
client.connect(MQTT_BROKER)

teller = 1
while True:
    sensorNum = random.randint(1, 7)
    country = random.choice(COUNTRIES)
    topic1 = f"{country}/{TEMPERATURE}/{SENSOR} {sensorNum}"
    topic2 = f"{country}/{HUMIDITY}/{SENSOR} {sensorNum}"
    topic3 = f"{country}/{PRESSURE}/{SENSOR} {sensorNum}"
    client.publish(topic1,  random.uniform(10, 25) )
    client.publish(topic2,  random.uniform(0, 100) )
    client.publish(topic3,  random.uniform(0.9, 1.1) )
 
    print(f"Published : {teller} {country} {sensorNum}")
    teller = teller + 1
    time.sleep(.2)
    
