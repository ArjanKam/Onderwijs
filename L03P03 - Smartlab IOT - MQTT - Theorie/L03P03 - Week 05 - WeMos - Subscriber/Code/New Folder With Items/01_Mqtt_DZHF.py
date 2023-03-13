# Complete project details at https://RandomNerdTutorials.com
import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network

#setup garbidge collection
import esp
esp.osdebug(None)
import gc
gc.collect()

#init constants
SSID           = "duurzaamheidsfabriek"
SSID_PASSWORD  = "DZHFquest"

TOPIC_SUBSCRIBE= b'Nederland/TEMPERATURE/Sensor 1'
MQTT_BROKER    = "192.168.2.128"
SLEEP          = 1
KEEPALIVETIME = 10 # <------------- of 60....???
SLEEP_RECONNECT= 10
CLIENT_ID      = ubinascii.hexlify(machine.unique_id())
  
def on_message(topic, msg):
    topics = topic.decode('utf-8').split('/')
    data = msg.decode('utf-8')
    temperature = round(float(data), 2)
    print(topics[0], topics[1], topics[2], temperature)
    #handle_measurement(topics[0], topics[1], topics[2], temperature )

def connect_and_subscribe():
    client = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=KEEPALIVETIME)
    client.set_callback(on_message)
    client.connect()
    client.subscribe(TOPIC_SUBSCRIBE)
    print("Connected to %s MQTT broker, subscribed to %s topic" %(MQTT_BROKER, TOPIC_SUBSCRIBE))
    return client

def start():
    station = network.WLAN(network.STA_IF)
    station.disconnect()
    print('Start Connecting')
    print(station.ifconfig())
    
    station.active(False)
    while station.active():
        time.sleep(SLEEP)
    station.active(True)
    station.connect(SSID, SSID_PASSWORD)
    while station.isconnected() == False:
        print('.', end = "")
        time.sleep(SLEEP)

    print('\nConnection successful')
    print(station.ifconfig())
    
def restart_and_reconnect():
    global client
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(SLEEP_RECONNECT)
    start()
    client = connect_and_subscribe()

start()
client = connect_and_subscribe()
while True:
  try:
    client.check_msg()
  except OSError as e:
    restart_and_reconnect()