import machine
import network
import utime
from umqttsimple import MQTTClient

SSID     = "ESA"
PASSWORD = "Tn09Q4233_"
TOPIC = "DZHF/ARJAN/TEMPERATURE"
MQTT_BROKER = "192.168.2.128"
SLEEP = 5
station = network.WLAN(network.STA_IF)
station.active(True)

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
        utime.sleep(SLEEP)
        
        