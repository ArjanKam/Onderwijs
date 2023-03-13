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
SSID           = "ESA"
SSID_PASSWORD  = "Tn09Q4233_"

TOPIC_SUBSCRIBE= b'DZHF/TEMPERATURE/+'
TOPIC_PUBISH   = b'notification'
MQTT_BROKER    = "192.168.2.128"
SLEEP          = 2
CLIENT_ID      = ubinascii.hexlify(machine.unique_id())

#init global variables
last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(SSID, SSID_PASSWORD)

while station.isconnected() == False:
  print('.', end = "")
  time.sleep(0.5)
  pass

print('\nConnection successful')
print(station.ifconfig())

def on_message(topic, msg):
  topics = topic.decode('utf-8').split('/')
  data = msg.decode('utf-8')
  temperature = round(float(data), 2)
  print(topics[2], temperature)

def connect_and_subscribe():
  client = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=10)
  client.set_callback(on_message)
  client.connect()
  client.subscribe(TOPIC_SUBSCRIBE)
  print("Connected to %s MQTT broker, subscribed to %s topic" %(MQTT_BROKER, TOPIC_SUBSCRIBE))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    client.check_msg()
    if (time.time() - last_message) > message_interval:
      message = b'Hello #%d' % counter
      client.publish(TOPIC_PUBISH, message)
      last_message = time.time()
      counter += 1
  except OSError as e:
    restart_and_reconnect()