import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import logging

MQTT_BROKER = "192.168.1.99"

def on_connect(client, userdata, flags, rc):
     logging.info("Connected flags"+str(flags)+"result code "\
     +str(rc)+" client1_id ")
     client.connected_flag=True
     
def on_log(client,userdata,level,buff):
    logging.info(buff)

logging.basicConfig(level = logging.INFO )
client = mqtt.Client("Pubisher")
client.on_connect = on_connect
client.on_log = on_log
client.connect( MQTT_BROKER )
client.loop_start()

def measureTemperature():
    return uniform(20.0, 21.0)

def klepstatus():
    if measureTemperature() > 20.5:
        return ("open")
    else:
        return ("closed")

while True:
    temperature = measureTemperature()
    flow = klepstatus()
    client.publish("Groep1/Aardvochtigheid", temperature)
    #client.publish("Groep1/klepstatus", flow)
    time.sleep(2)
    
client.disconnect()
client.loop_stop()
