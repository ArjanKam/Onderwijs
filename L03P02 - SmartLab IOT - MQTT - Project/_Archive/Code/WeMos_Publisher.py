import machine
import network
import ubinascii     # new
import utime
import random
from umqttsimple import MQTTClient

CLIENT_ID = ubinascii.hexlify(machine.unique_id()) # new
#2.4 GHz
SSID     = "MQTT_WIFI"
SSID_PASSWORD = "kambergArjan"

MQTT_BROKER    = "192.168.1.99"
TOPIC = "DZHF/ARJAN/TEMPERATURE"        # new
TOPIC_COUNT = "DZHF/ARJAN/COUNTER"        # new
SLEEP = 2
station = network.WLAN(network.STA_IF)
station.active(True)

def get_Measurements():          # new
    return str(random.getrandbits(8))

def callback_data(topic, msg):   # new
    print(topic, msg)

def connect():                   # new2
    client = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=10)
    client.set_callback(callback_data)
    print("Trying to connect to broker")
    client.connect()
    print("Connection successfull")
    return client

counter = 1
while True:
    if not station.isconnected():
        print(counter, "connecting...")
        counter = counter + 1
        station.connect(SSID, SSID_PASSWORD)
        utime.sleep(SLEEP)
        
    while station.isconnected():
        print("Connected !")
        print(station.ifconfig())
# ----- new
        try:
            client = connect() 
            countdown = 100
            while countdown > 0:
                print(countdown)
                countdown = countdown - 1
                client.publish(TOPIC_COUNT, str(countdown))
                client.publish(TOPIC, get_Measurements())
                utime.sleep(SLEEP)
        except OSError as e:
            print(e)
# ------ end new            
        utime.sleep(SLEEP)
        
        