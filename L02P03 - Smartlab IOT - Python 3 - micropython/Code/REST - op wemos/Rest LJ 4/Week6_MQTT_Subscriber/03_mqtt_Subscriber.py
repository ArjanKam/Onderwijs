import paho.mqtt.client as mqtt
import time
TOPIC = "DZHF/ARJAN/TEMPERATURE"
#MQTT_BROKER = "localhost"
#MQTT_BROKER = "test.mosquitto.org"
MQTT_BROKER = "10.7.2.109"

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))
    
client = mqtt.Client("Smartphone")
client.connect( MQTT_BROKER ) 

client.loop_start()

client.subscribe(TOPIC)
client.on_message=on_message 

time.sleep(180)
client.loop_stop()

