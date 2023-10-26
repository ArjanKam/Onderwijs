import machine
import network
import utime

SSID     = "duurzaamheidsfabriek"
PASSWORD = "DZHFquest"
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
        
        