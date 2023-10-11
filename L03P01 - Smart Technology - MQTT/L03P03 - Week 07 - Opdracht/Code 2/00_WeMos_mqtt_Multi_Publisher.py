import machine
from Leds import leds, allLedsOff
import network
import ubinascii     # new
import utime
import random
from umqttsimple import MQTTClient

LUCHTVOCHTIGHEID = "LUCHTVOCHTIGHEID"

CLIENT_ID = ubinascii.hexlify(machine.unique_id()) # new
#2.4 GHz
SSID     = "MQTT_WIFI"
SSID_PASSWORD = "kambergArjan"

MQTT_BROKER    = "192.168.1.99"
SLEEP = 2
                    
station = network.WLAN(network.STA_IF)
station.active(True)

def uniform(minValue, maxValue):
    value = minValue + (random.getrandbits(8) * (maxValue - minValue) / 256)
    return str(value)

def sensor():
    return str("Sensor " + str(random.getrandbits(2)))

def publishValue(client, location, humidityMinMax, pressureMinMax, tempMinMax):
    client.publish(location + "/LUCHTVOCHTIGHEID/"+ sensor(),  uniform(humidityMinMax[0], humidityMinMax[1]) )
    client.publish(location + "/PRESSURE/"+ sensor(),  uniform(pressureMinMax[0], pressureMinMax[1]) )
    client.publish(location + "/TEMPERATURE/"+ sensor(),  uniform(tempMinMax[0], tempMinMax[1]) )

def callback_data(topic, msg):   # new
    print(topic, msg)

def connect():                   # new2
    client = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=10)
    client.set_callback(callback_data)
    print("Trying to connect to broker")
    client.connect()
    print("Connection successfull")
    return client

counter = 1
while True:
    if not station.isconnected():
        leds[counter % 8].on()
        print(counter, "connecting...")
        station.connect(SSID, SSID_PASSWORD)
        utime.sleep(SLEEP)
        leds[counter % 8].off()
        counter = counter + 1
        
    while station.isconnected():
        print("Connected !")
        print(station.ifconfig())
# ----- new
        try:
            client = connect() 
            countdown = 100
            while True:
                leds[0].on()
                publishValue(client, "Nederland", (50, 100), (900, 1100), (10, 20))
                leds[1].on()
                publishValue(client, "Belgie", (50, 80), (900, 1100), (10, 20))
                publishValue(client, "Duitsland", (30, 80), (900, 1100), (10, 20))
                leds[2].on()
                publishValue(client, "Engeland", (0, 30), (900, 1100), (10, 20))
                leds[3].on()
                publishValue(client, "Frankrijk", (0, 40), (900, 1100), (20, 30))
                leds[4].on()
                publishValue(client, "Luxemburg", (80, 100), (900, 1100), (20, 30))
                publishValue(client, "Spanje", (0, 30), (900, 1100), (20, 40))
                leds[5].on()
                publishValue(client, "Italie", (0, 30), (900, 1100), (20, 40))
                leds[6].on()
                publishValue(client, "Noorwegen", (80, 100), (.9, 1.100), (0, 10))
                leds[7].on()
                publishValue(client, "Denemarken", (80, 100), (900, 1100), (0, 10))
                leds[8].on()
                publishValue(client, "Zweden", (70, 100), (900, 1100), (10, 15))
                
                print("Published")
                allLedsOff()
                utime.sleep(SLEEP)
        except OSError as e:
            pins[4].on()
            print(e)
# ------ end new            
        utime.sleep(SLEEP)
        