import paho.mqtt.client as mqtt
import time

TOPIC = [("DZHF/TEMPERATURE/+", 0)] #, ("DZHF/+/PRESSURE", 0)
MQTT_BROKER = "192.168.1.99"
CLIENT_NAME = "Logger"
def on_message(client, userdata, message):
    print(f"received message: {message.topic}", message.payload.decode("utf-8"))
    
client = mqtt.Client(CLIENT_NAME)
client.connect(MQTT_BROKER)

client.loop_start()

client.subscribe(TOPIC)
client.on_message=on_message 

time.sleep(10)
client.loop_stop()

