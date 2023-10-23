import paho.mqtt.client as mqtt
import time
from datetime import datetime
import csv

SSID = "MQTT_WIFI"
PASSWORD = "kambergArjan"
TOPIC = ("G7/+", 0)
#TOPIC2 = ("G7/Moisture",0)
MOISTURE = "MOISTURE"
VALVE = "VALVE"
MQTT_BROKER = "192.168.1.99"
CLIENT_NAME = "Logger007"
FILE_LOCATION = r"C:\Bewatering_systeem\Bewatering.csv"
last_valve = None
last_moisture = None

def writeToFile(tijd, last_moisture, last_valve):
    f = open(FILE_LOCATION,'a', encoding='UTF8', newline="")
    writer = csv.writer(f)
    data = "{0};{1};{2}".format(tijd, last_moisture, last_valve)
    writer.writerow([data])
    f.close()
    
def on_message(client, userdata, message):
    global last_valve, last_moisture
    
    tijd = datetime.now()
    topic = message.topic.split('/')
    temp = message.payload.decode("utf-8")
    
    #print(topic)
    if topic[1] == MOISTURE:
        last_moisture = temp
    if topic[1] == VALVE:
        last_valve = temp
    print(tijd, topic, temp, last_moisture, last_valve)
    writeToFile(tijd, last_moisture, last_valve)
    
client = mqtt.Client(CLIENT_NAME)
client.connect(MQTT_BROKER)


client.loop_start()

client.subscribe(TOPIC)
# client.subscribe(TOPIC2)
client.on_message=on_message 

while True:
    #pass # do not use pass... to much CPU consumption
    print(".", end="")
    time.sleep(10)
    
#client.loop_stop()

