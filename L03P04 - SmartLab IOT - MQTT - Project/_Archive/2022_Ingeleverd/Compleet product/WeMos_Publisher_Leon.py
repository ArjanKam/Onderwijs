import machine
import network
import ubinascii     # new
import utime
from machine import Pin, ADC
from umqttsimple import MQTTClient

CLIENT_ID = ubinascii.hexlify(machine.unique_id()) # new
#2.4 GHz
SSID     = "MQTT_WIFI"
PASSWORD = "kambergArjan"
TOPIC = "Groep 5/Waterlevel"
TOPIC2 = "Groep 5/Klep"
MQTT_BROKER = "192.168.1.99"           # new
SLEEP = 5
p2 = Pin(2, Pin.IN, Pin.PULL_UP)
soil = ADC(0)
min_moisture=0
max_moisture=65535
readDelay = 0.5
station = network.WLAN(network.STA_IF)
station.active(True)
relay = Pin(5, Pin.OUT)
regelklep_rood = Pin(15, Pin.OUT)
regelklep_groen = Pin(14, Pin.OUT)

def get_Measurements():          # new
    moisture = ((max_moisture-soil.read_u16())*100/(max_moisture-min_moisture))
    return moisture

def measure_Valve():
    return p2.value()

def callback_data(topic, msg):# new
    klep = str(msg)
    if klep == "b'Close'":
        print("Close")
        relay.value(0)
        regelklep_rood(1)
        regelklep_groen(0)

    if klep == "b'Open'":
        print("Open")
        relay.value(1)
        regelklep_groen(1)
        regelklep_rood(0)
def connect():                   # new
    client = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=60)
    client.set_callback(callback_data)
    client.connect()
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
# ----- new
        try:
            client = connect() 
            countdown = 100
            while countdown > 0:
                data = get_Measurements()
                #logger = on_message(client, get_Measurements(), "hi")
                client.publish(TOPIC, str(data))
                client.subscribe(TOPIC2)
                print(("moisture: " +"%.2f" % data +"%"))
                utime.sleep(SLEEP)
                countdown = countdown - 1
        except OSError as e:
            print(e)
# ------ end new            
        utime.sleep(SLEEP)
                