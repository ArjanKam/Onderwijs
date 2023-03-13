import network
import urequests
import utime
#2.4Ghz networks only
SSID     = ""
PASSWORD = ""

station = network.WLAN(network.STA_IF)
while station.active():
    station.active(False)
    utime.sleep(1)
    
station.active(True)
station.active()

station.connect(SSID, PASSWORD)

print("Internal ip = ", station.ifconfig())
print("Connecting  = ", end= "")
while not station.isconnected():
    print(".", end = "")
    utime.sleep(1)

print("Internal ip = ", station.ifconfig())
print("connected   = ", station.isconnected())
print("External ip = ", urequests.get('http://api.ipify.org/').text)