import paho.mqtt.client as mqtt
import time
import uuid
import file_export as export

TOPIC = [("+/+/+", 0), ("+/+/+", 0)]
MQTT_BROKER = "10.9.59.209"
CLIENT_NAME = str(uuid.uuid4())
   
def on_message(client, userdata, message):
    topics = message.topic.split('/')
    msg = message.payload.decode('utf-8')
    export.write_to_csv(topics, msg)
    #export.write_to_json(topics, msg)
    
client = mqtt.Client(CLIENT_NAME)
client.connect(MQTT_BROKER)

client.loop_start()

client.subscribe(TOPIC)
client.on_message=on_message 

while True:
    #pass # do not use pass... to much CPU consumption
    time.sleep(10)
    
client.loop_stop()



