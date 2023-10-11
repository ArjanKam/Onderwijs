import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import logging
TOPIC = "DZHF/ARJAN/TEMPERATURE"
MQTT_BROKER = "localhost"

def on_connect(client, userdata, flags, rc):
     logging.info("Connected flags"+str(flags)+"result code "\
     +str(rc)+" client1_id ")
     client.connected_flag=True
     
def on_log(client,userdata,level,buff):
    logging.info(buff)

def on_message(client,userdata,msg):
    logging.info("Topic " + msg.topic + " Message:" + str(msg.payload))
    
logging.basicConfig(level = logging.INFO )
client = mqtt.Client("Pubisher")
client.on_connect = on_connect
client.on_log = on_log
client.on_message = on_message
client.connect( MQTT_BROKER )
client.subscribe( TOPIC )
client.loop_start()

def measureTemperature():
    return uniform(20.0, 21.0)

countdown = 100
while countdown > 0:
    temperature = measureTemperature()
    client.publish(TOPIC, temperature)
    time.sleep(2)
    countdown = countdown - 1
client.disconnect()
client.loop_stop()
