import machine
import network
import utime
import ubinascii     # new
from umqttsimple import MQTTClient
import Secrets_kmb as Secrets
import MeasureTemp as Measure

MQTT_BROKER = "192.168.130.70"
SLEEP = 5
CLIENT_ID = ubinascii.hexlify(machine.unique_id()) # new
#print(CLIENT_ID)
ledInternal = machine.Pin("LED", machine.Pin.OUT)
ledInternal.off()
station = network.WLAN(network.STA_IF)
station.active(True)
station.disconnect()
counter = 1

def connectMqtt():                   # new
    client = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=60)
    client.connect()
    return client

while True:
    if not station.isconnected():
        print(counter, "connecting...")
        counter = counter + 1
        station.connect(Secrets.SSID, Secrets.PASSWORD)
        utime.sleep(SLEEP)
        ledInternal.toggle()
        
    while station.isconnected():
        print("Connected !")
        print(station.ifconfig())
        utime.sleep(SLEEP)
        ledInternal.on()
         
        try:
            client = connectMqtt()
            
            #returns list of tuples with Topic and data
            for data in Measure.whatToSend():
                client.publish(data[0], str(data[1]))

        except OSError as e:
            print(e)
        
        