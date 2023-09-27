import time
import dht
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
SSID           = "MQTT_WIFI"
SSID_PASSWORD  = "kambergArjan"

CLIENT_ID      = ubinascii.hexlify(machine.unique_id())
TOPIC_SUBSCRIBE= b'DZHF/+/+'
TOPIC_PUBLISHER_T= b'AK/SENSOR/TEMPERATURE'
TOPIC_PUBLISHER_H= b'AK/SENSOR/HUMIDITY'
MQTT_BROKER    = "192.168.1.99"

SLEEP          = 1
SLEEP_RECONNECT= 10

def connect_wifi():
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(SSID, SSID_PASSWORD)
    while station.isconnected() == False:
      print('.', end = "")
      time.sleep(SLEEP)
      pass
    print('\nConnected with', station.ifconfig())
    return station

def on_message(topic, msg):
  topics = topic.decode('utf-8').split('/')
  data = msg.decode('utf-8')
  temperature = round(float(data), 2)
  print(topics[0], topics[1], topics[2], temperature)

def connect_and_subscribe():
  client = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=60)
  client.set_callback(on_message)
  client.connect()
  client.subscribe(TOPIC_SUBSCRIBE)
  print("Connected {} to MQTT broker on : ", MQTT_BROKER )
  print("subscribed to topic: %s" %(TOPIC_SUBSCRIBE))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(SLEEP_RECONNECT)
  return connect_and_subscribe()

sensor = dht.DHT22(machine.Pin(4))
def measure_temp_hum():
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print(temp, hum)
    
station = connect_wifi()
client = None
while True:
  try:
      measure_temp_hum()
  except OSError as e:
    pass
    
  try:
    
    if client == None:
        client = restart_and_reconnect()
    else:
        result = client.check_msg()
        
  except OSError as e:
    print( e)
    client = None
