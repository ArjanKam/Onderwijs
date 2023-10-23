import paho.mqtt.client as mqtt
import time
from datetime import datetime
import csv

SSID = "MQTT_WIFI"
PASSWORD = "kambergArjan"
TOPIC = [("Groep 6/+", 0)]
WATERLEVEL = "Waterlevel"
KLEP = "Klep"
MQTT_BROKER = "192.168.1.99"
CLIENT_NAME = "Logger001"
FILE_LOCATION = 'C:/Users/Noah_/OneDrive/Documenten/Davinci/3e klas/IOT/Project water/Officele/groep6_logger.csv'
last_klepstand = None
last_waterlevel = None

def writeToFile(tijd, last_waterlevel, last_klepstand):
    f = open(FILE_LOCATION,'a', encoding='UTF8', newline="")
    writer = csv.writer(f)
    data = "{0};{1};{2}".format(tijd, last_waterlevel, last_klepstand)
    writer.writerow([data])
    f.close()
    
def on_message(client, userdata, message):
    global last_klepstand, last_waterlevel
    
    tijd = datetime.now()
    topic = message.topic.split('/')
    temp = message.payload.decode("utf-8")
    #print(topic)
    if topic[1] == WATERLEVEL:
        last_waterlevel = temp
    if topic[1] == KLEP:
        last_klepstand = temp
    print(tijd, topic, temp, last_waterlevel, last_klepstand)
    writeToFile(tijd, last_waterlevel, last_klepstand)
    
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
    
client.loop_stop()
