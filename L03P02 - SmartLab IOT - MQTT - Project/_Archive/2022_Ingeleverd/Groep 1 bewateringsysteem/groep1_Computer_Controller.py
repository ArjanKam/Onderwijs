import paho.mqtt.client as mqtt
import time
from datetime import datetime
import csv

TOPIC_KLEP = "Groep1/klepstatus"
TOPIC_MOISTURE = "Groep1/Aardvochtigheid"
MQTT_BROKER = "192.168.1.99"
CLIENT_NAME = "Groep1_jordi"


def on_message(client, userdata, message):
    nu = datetime.now().strftime("%D %H:%M:%S")
    topic = message.topic.split('/')
    moisture = message.payload.decode("utf-8")
    print(moisture)
    if float(moisture) < 20.5:
        client.publish(TOPIC_KLEP, "open")
        print("open")
    else:
        client.publish(TOPIC_KLEP, "closed")
        print("dicht")

client = mqtt.Client(CLIENT_NAME)
client.connect(MQTT_BROKER)

client.loop_start()

client.subscribe(TOPIC_MOISTURE)
client.on_message=on_message 


while True:
    #pass # do not use pass... to much CPU consumption
    print(".", end="")
    time.sleep(10)
        
client.loop_stop()

