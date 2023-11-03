import machine
import network
import utime
from umqttsimple import MQTTClient
import Secrets_DZHF as Secrets
import ubinascii

TOPIC = "DZHF/ARJAN/TEMPERATURE"
MQTT_BROKER = "192.168.65.70"
SLEEP = 5
CLIENT_ID      = ubinascii.hexlify(machine.unique_id())
TOPIC_SUBSCRIBE= b'Nederland/+/+'
SLEEP_RECONNECT= 10

station = network.WLAN(network.STA_IF)
station.active(True)

def on_message(topic, msg):
  topics = topic.decode('utf-8').split('/')
  data = msg.decode('utf-8')
  print(topics[0], topics[1], topics[2], data)
  temperature = round(float(data), 2)
  
counter = 1
while not station.isconnected():
        print(counter, "connecting...")
        counter = counter + 1
        station.connect(Secrets.SSID, Secrets.PASSWORD)
        utime.sleep(SLEEP)
        
if station.isconnected():
    print("Connected !")
    print(station.ifconfig())
    
    client = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=60)
    client.set_callback(on_message)
    client.connect()
    client.subscribe(TOPIC_SUBSCRIBE)
    print("Connected {} to MQTT broker on : ", MQTT_BROKER )
    print("subscribed to topic: %s" %(TOPIC_SUBSCRIBE))

    while True:
        try:
            result = client.check_msg()
        except OSError as e:
            print( e)
    

