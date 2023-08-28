import paho.mqtt.client as mqtt
import time

TOPIC = [("DZHF/TEMPERATURE/Sensor 1", 0)]
MQTT_BROKER = "192.168.1.81"
CLIENT_NAME = "Logger"
def on_message(client, userdata, message):
    topic = message.topic.split('/')
    temp = message.payload.decode("utf-8")
    print(f"{topic[1]} {topic[2]} : {temp}")

client = mqtt.Client(CLIENT_NAME)
client.connect(MQTT_BROKER)

client.loop_start()

client.subscribe(TOPIC)
client.on_message=on_message 

while True:
    #pass # do not use pass... to much CPU consumption
    time.sleep(10)
client.loop_stop()

