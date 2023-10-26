import paho.mqtt.client as mqtt
import time

TOPIC = "TEMPERATURE"
MQTT_BROKER = "192.168.1.99"
CLIENT_NAME = "Logger"


def on_message(client, userdata, message):
    print("received message: ", str(message.payload.decode("utf-8")))


client = mqtt.Client(CLIENT_NAME)
client.connect(MQTT_BROKER)

client.loop_start()

client.subscribe(TOPIC)
client.on_message = on_message

time.sleep(10)
client.loop_stop()
