# Complete project details at https://RandomNerdTutorials.com
import machine
import micropython
import network
import time
from umqttsimple import MQTTClient
import Secrets_Asus as secrets
#import Secrets_SmartLab as secrets

#setup garbidge collection
#import esp
#esp.osdebug(None)
#import gc
#gc.collect()

MQTT_BROKER    = "192.168.1.124"
TOPIC_SUBSCRIBE= b'Nederland/PRESSURE/+'
MIN_VALUE      = "min"
MAX_VALUE      = "max"
SLEEP          = 1
SLEEP_RECONNECT= 10

__values = {}
def handle_measurement(main, measure, sensor, value):
    global __values
    if not sensor in __values:
        __values[sensor] = {MIN_VALUE: value, MAX_VALUE: value}
    message = ""
    if __values[sensor][MIN_VALUE] > value:
        __values[sensor][MIN_VALUE] = value
        message = "<-- New min value"
    elif __values[sensor][MAX_VALUE] < value:
        __values[sensor][MAX_VALUE] = value
        message = "<-- New max value"
    print(sensor, __values[sensor][MIN_VALUE], __values[sensor][MAX_VALUE], value, message)
    
def on_message(topic, msg):
  topics = topic.decode('utf-8').split('/')
  data = msg.decode('utf-8')
  temperature = round(float(data), 2)
  print(topics[0], topics[1], topics[2], temperature)
  #handle_measurement(topics[0], topics[1], topics[2], temperature )

def connect_and_subscribe():
  client = MQTTClient(secrets.CLIENT_ID, MQTT_BROKER, keepalive=60)
  client.set_callback(on_message)
  client.connect()
  client.subscribe(TOPIC_SUBSCRIBE)
  print("Connected to %s MQTT broker, subscribed to %s topic" %(MQTT_BROKER, TOPIC_SUBSCRIBE))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(SLEEP_RECONNECT)
  machine.reset()

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(secrets.SSID, secrets.SSID_PASSWORD)

while station.isconnected() == False:
  print('.', end = "")
  time.sleep(SLEEP)
  pass

print('\nConnection successful')
print(station.ifconfig())

try:
    client = connect_and_subscribe()
except OSError as e:
    print( e.errno)
    restart_and_reconnect()

while True:
  try:
    client.check_msg()
  except OSError as e:
    print( e)
    restart_and_reconnect()
