import paho.mqtt.client as mqtt
import time
from datetime import datetime
import csv

TOPIC = [("Groep1/+", 0)]
#TOPIC = [("DZHF/TEMPERATURE/Sensor 1", 0)]
MQTT_BROKER = "192.168.1.99"
CLIENT_NAME = "Groep1_jordi"

last_klepstand = ""
last_waterlevel = 0
def on_message(client, userdata, message):
    global last_klepstand, last_waterlevel
    f = open('groep1_logger.csv','a', encoding='UTF8', newline='')
    writer = csv.writer(f)
    
    nu = datetime.now().strftime("%D %H:%M:%S")
    topic = message.topic.split('/')
    temp = message.payload.decode("utf-8")
    
    if topic[1] == "Aardvochtigheid":
        last_waterlevel = temp
    if topic[1] == "klepstatus":
        last_klepstand = temp
    
    print(topic, temp)
    writer.writerow([nu, last_klepstand, last_waterlevel])
    f.close()

client = mqtt.Client(CLIENT_NAME)
client.connect(MQTT_BROKER)

client.loop_start()

client.subscribe(TOPIC)
client.on_message=on_message 


while True:
    #pass # do not use pass... to much CPU consumption
    time.sleep(10)
        
client.loop_stop()

