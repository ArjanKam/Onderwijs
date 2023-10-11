import paho.mqtt.client as mqtt
import time

TOPIC = [("DZHF/TEMPERATURE/Sensor 1", 0)]
MQTT_BROKER = "192.168.2.128"
CLIENT_NAME = "Logger"

minTemp = None
maxTemp = None
meting = 1
def on_message(client, userdata, message):
    global minTemp, maxTemp, meting
    topic = message.topic.split('/')
    temp = message.payload.decode("utf-8")
    temp = round(float(temp), 2)
    message = ""
    if minTemp == None or temp < minTemp:
        minTemp = temp;
        message = "<---- New Min Temperature"
    if maxTemp == None or temp > maxTemp:
        maxTemp = temp;
        message = "<---- New Max Temperature"
    print(f"{topic[1]} {topic[2]} : {meting} {minTemp} {maxTemp} {temp} {message}")
    meting = meting + 1

client = mqtt.Client(CLIENT_NAME)
client.connect(MQTT_BROKER)

client.loop_start()

client.subscribe(TOPIC)
client.on_message=on_message 

while True:
    #pass # do not use pass... to much CPU consumption
    time.sleep(10)
    
client.loop_stop()

