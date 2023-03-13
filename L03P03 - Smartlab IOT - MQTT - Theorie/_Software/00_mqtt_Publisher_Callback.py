import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import logging
TOPIC = "DZHF/ARJAN/TEMPERATURE"
"192.168.1.99"

def measureTemperature():
    return uniform(20.0, 21.0)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        logging.info("Connected flags"+str(flags)+"result code "\
            +str(rc)+" client1_id ")
        client.connected_flag=True
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)
     
def on_log(client,userdata,level,buff):
    logging.info(buff)
    
logging.basicConfig(level = logging.INFO )
client = mqtt.Client("Pubisher")
client.on_connect = on_connect
client.on_log = on_log

client.loop_start()
client.connect( MQTT_BROKER )

countdown = 100
while countdown > 0:
    temperature = measureTemperature()
    client.publish(TOPIC, temperature)
    time.sleep(2)
    countdown = countdown - 1
client.disconnect()
client.loop_stop()
