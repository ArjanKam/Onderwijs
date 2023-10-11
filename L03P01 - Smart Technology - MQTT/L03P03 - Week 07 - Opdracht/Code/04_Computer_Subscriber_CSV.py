import paho.mqtt.client as mqtt
import time
import csv

TOPIC = [("DZHF/TEMPERATURE/Sensor 1", 0)]
MQTT_BROKER = "192.168.2.128"
CLIENT_NAME = "Logger"
CSV_FILE = "test.csv"
#kolommen is een tuple
def writeTupleToFile(file, kolommen):
    f = open(file,'a', encoding='UTF8', newline="")
    writer = csv.writer(f)
    data = ""
    for kolom in kolommen:
        data = data + "{0};".format(kolom)
    writer.writerow([data])
    f.close()

TOPIC_1     = "Moisture"
TOPIC_2     = "Klepstand"
last_klep   = ""
last_moisture = ""
def parseMoistureKlep(sensor, value)
    if sensor == TOPIC_1:
        last_moisture = value
    if sensor == TOPIC_2:
        last_klep = value
    huidigeTijd = "00:00:00"
    writeTupleToFile(CSV_FILE, (huidigeTijd, last_moisture, last_klep))
    
def on_message(client, userdata, message):
    topic = message.topic.split('/')
    temp = message.payload.decode("utf-8")
    parseMoistureKlep(topic[2], temp)
    
client = mqtt.Client(CLIENT_NAME)
client.connect(MQTT_BROKER)

client.loop_start()

client.subscribe(TOPIC)
client.on_message=on_message 

while True:
    #pass # do not use pass... to much CPU consumption
    time.sleep(10)
client.loop_stop()

