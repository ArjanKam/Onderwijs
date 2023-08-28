import machine
import network
import ubinascii     # new
import utime
from machine import Pin, ADC
from umqttsimple import MQTTClient

led = Pin(15, Pin.OUT)

CLIENT_ID = ubinascii.hexlify(machine.unique_id()) # new
#2.4 GHz
SSID     = "MQTT_WIFI"
PASSWORD = "kambergArjan"
TOPIC = "Groep 1/Vochtigheid"
TOPIC2 = "Groep 1/Klep"
MQTT_BROKER = "192.168.1.99"           # new
SLEEP = 5
readDelay = 0.5
station = network.WLAN(network.STA_IF)
station.active(True)
adc = ADC(0) 

def get_Measurements():          # new
    moisture = adc.read()
    return moisture

def callback_data(topic, msg):# new
    print(str(msg))
    
    if str(msg) == "b'open'":
        led.on()
        
    if str(msg) == "b'closed'":
        led.off()

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
            countdown = 10
            while countdown > 0:
                data = get_Measurements()
                #logger = on_message(client, get_Measurements(), "hi")
                client.publish(TOPIC, str(data))
                
                if data > 700:
                    client.publish(TOPIC2, "open")
                else:
                    client.publish(TOPIC2, "closed")
                
                client.subscribe(TOPIC2)
                print(("moisture: " +"%.2f" % data))
                utime.sleep(SLEEP)
                countdown = countdown - 1
        except OSError as e:
            print(e)
# ------ end new            
        utime.sleep(SLEEP)
                