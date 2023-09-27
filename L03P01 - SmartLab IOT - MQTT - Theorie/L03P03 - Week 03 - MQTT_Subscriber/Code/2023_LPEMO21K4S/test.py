import paho.mqtt.client as mqtt
import time
import uuid

TOPIC = [("Belgie/Temperature/+", 0), ("Nederland/Humidity/+", 0)]
MQTT_BROKER = "10.9.51.168"
CLIENT_NAME = str(uuid.uuid4())
CSV_HEADER = "MetingId; Land; Element; Sensor; Waarde"
    
def on_message(client, userdata, message):
    topics = message.topic.split('/')
    msg = message.payload.decode('utf-8')
    write_to_csv(topics, msg)
    
client = mqtt.Client(CLIENT_NAME)
client.connect(MQTT_BROKER)

client.loop_start()

client.subscribe(TOPIC)
client.on_message=on_message 

while True:
    #pass # do not use pass... to much CPU consumption
    time.sleep(10)
    
client.loop_stop()



