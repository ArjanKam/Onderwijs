import machine
import time
import BlynkLib
from ULTRASONE_HC_SR04_DOCENT import HCSR04
from ActualSunRise import ActualSunRise

WIFI_SSID     = "ESA_2_4GHz" #"<YOUR WIFI SSID>"
WIFI_PASSWORD = "S1m30nElsA6213" #"<YOUR WIFI PASSWORD>"
BLYNK_AUTH    = 'IFD3NI0oBH3agF_cu3bPL85Axj0e8XeY'

MAX_DISTANCE= 100  # 
SLEEP       = 1000 # 1 seconden
PIN_ECHO    = 4    # Pin van dre Echo
PIN_TRIGGER = 5    # PIN van de trigger
PIN_LEDSTRIP= 16   # GPIO16 on WeMos voor LEDSTRIP

print("Getting local information")
ledStrip = machine.Pin( PIN_LEDSTRIP, machine.Pin.OUT )
ultrasonic = HCSR04(trigger_pin=PIN_TRIGGER, echo_pin=PIN_ECHO, echo_timeout_us=1000000)
sun = ActualSunRise(WIFI_SSID, WIFI_PASSWORD)

print("Connecting to Blynk...")
blynk = BlynkLib.Blynk(BLYNK_AUTH) # , log=print

blinkLedStatus = False    # Blynk LED status
lastLedOn = None
lastDistance = None

# Register Virtual Pins
@blynk.VIRTUAL_WRITE(0)
def my_write_handler(value):
    global blinkLedStatus
    #print('Current V1 value: {}'.format(value))
    if value[0] == '0':
        blinkLedStatus = False
    else:
        blinkLedStatus = True

@blynk.VIRTUAL_READ(1)
def my_read_handler():
    # this widget will show some time in seconds..
    if lastLedOn:
        blynk.virtual_write(1, 255)
    else:
        blynk.virtual_write(1, 0)
    
@blynk.on("connected")
def blynk_connected(ping):
    print('Blynk ready. Ping:', ping, 'ms')

def equalWithMarge(value1, value2, marge):
    if value1 == None or value2 == None:
        return False
    if (value1 + marge) < value2:
        return False
    if (value1 - marge) > value2:
        return False
    return True

def runLoop():
    global lastLedOn
    global lastDistance
    nearbyStatus = False      # Sensor LED status
    ledOn = False
    # Continually try to connect to WiFi access point
    while sun.connected():
        sunInfo = sun.info()
        distance = ultrasonic.distance_cm()
        
        if not equalWithMarge(lastDistance, distance, 2):
            lastDistance = distance
            print('Distance:', distance, 'cm', '| sunInfo =', sunInfo)
        
        blynk.run()
        
        nearbyStatus = distance <= MAX_DISTANCE and sunInfo[1]
        ledOn = nearbyStatus or blinkLedStatus
        if lastLedOn != ledOn:
            lastLedOn = ledOn
            if ledOn:
                ledStrip.on()
            else:
                ledStrip.off()
            
        machine.idle()

# Run blynk in the main thread:
runLoop()

        
