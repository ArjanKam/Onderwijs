import machine
import network
import utime
from umqttsimple import MQTTClient
import Secrets_Asus as secrets
import Secrets_SmartLab as secrets

#setup garbidge collection
#import esp
#esp.osdebug(None)
import gc
gc.collect()

MQTT_BROKER    = "192.168.1.99"
TOPIC = b"DZHF/TEMPERATURE/Sensor 1"
KEEPALIVETIME = 10 # <------------- of 60....???
SLEEP = 10
station = network.WLAN(network.STA_IF)
station.active(True)

def callback_data(topic, msg):
    print("-----------------")
    print(topic, msg)

def connect():
    client = MQTTClient(secrets.CLIENT_ID, MQTT_BROKER, keepalive=KEEPALIVETIME)
    client.set_callback(callback_data)
    client.connect()
    client.subscribe(TOPIC)
    return client

counter = 1
while True:
    if not station.isconnected():
        print(counter, "connecting...")
        counter = counter + 1
        station.connect(secrets.SSID, secrets.SSID_PASSWORD)
        utime.sleep(SLEEP)
        
    while station.isconnected():
        print("Connected !", CLIENT_ID, end="")
        print(station.ifconfig())
        
        try:
            client = connect()
            result = client.check_msg()
        except OSError as e:
            print(e)
            
        utime.sleep(SLEEP)
        
        