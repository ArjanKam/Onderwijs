import machine
import network
import ubinascii
import utime
from umqttsimple import MQTTClient

CLIENT_ID = ubinascii.hexlify(machine.unique_id())
#2.4 GHz
SSID     = "Kmb"
PASSWORD = "Welkom01"
TOPIC = "DZHF/ARJAN/TEMPERATURE"
MQTT_BROKER = "192.168.252.70"
SLEEP = 5
station = network.WLAN(network.STA_IF)
station.active(True)

def get_Measurements():
    return "hoi"

def callback_data(topic, msg):
    print(topic, msg)

def connect():
    client = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=60)
    client.set_callback(callback_data)
    print("Connecting with MQTT Broker")
    client.connect()
    print("Connected")
    return client

counter = 1
while True:
    if not station.isconnected():
        print(counter, "connecting...")
        counter = counter + 1
        station.connect(SSID, PASSWORD)
        utime.sleep(SLEEP)
        
    while station.isconnected():
        print("Connected !")
        print(station.ifconfig())

        try:
            client = connect()
            countdown = 100
            while countdown > 0:
                data = get_Measurements()
                print("Publish : " + data)
                client.publish(TOPIC, data)
                utime.sleep(SLEEP)
                countdown = countdown - 1
        except OSError as e:
            print(e)
            
        utime.sleep(SLEEP)
        
        