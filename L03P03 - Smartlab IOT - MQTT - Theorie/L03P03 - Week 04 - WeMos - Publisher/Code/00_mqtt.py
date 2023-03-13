import machine
import network
import utime
from umqtt.simple import MQTTClient
import Secrets_HZHF as Secrets

TOPIC = "DZHF/ARJAN/TEMPERATURE"
MQTT_BROKER = "192.168.1.124"
SLEEP = 5

station = network.WLAN(network.STA_IF)
station.active(True)

counter = 1
while True:
    if not station.isconnected():
        print(counter, "connecting...")
        counter = counter + 1
        station.connect(Secrets.SSID, Secrets.PASSWORD)
        utime.sleep(SLEEP)
        
    while station.isconnected():
        print("Connected !")
        print(station.ifconfig())
        utime.sleep(SLEEP)
        
        