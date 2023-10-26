import machine
import network
import ubinascii
import utime
from umqttsimple import MQTTClient

CLIENT_ID = ubinascii.hexlify(machine.unique_id())
SSID           = "MQTT_WIFI"
SSID_PASSWORD  = "kambergArjan"

MQTT_BROKER    = "192.168.1.99"
TOPIC = ""
MQTT_BROKER = ""
KEEPALIVETIME = 10
SLEEP = 5
station = network.WLAN(network.STA_IF)
station.active(True)

def callback_data(topic, msg):
    print(topic, msg)

def connect():
    client = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=KEEPALIVETIME)
    client.set_callback(callback_data)
    client.connect()
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

        try:
            client = connect()             
        except OSError as e:
            print(e)
        utime.sleep(SLEEP)
        
        