import machine
import time
from ULTRASONE_HC_SR04_DOCENT import HCSR04
from ActualSunRise import ActualSunRise

WIFI_SSID     = "<YOUR WIFI SSID>"
WIFI_PASSWORD = "<YOUR WIFI PASSWORD>"

MAX_DISTANCE= 100  # 
SLEEP       = 1000 # 1 seconden
PIN_ECHO    = 4    # Pin van dre Echo
PIN_TRIGGER = 5    # PIN van de trigger
PIN_LEDSTRIP= 16   # GPIO16 on WeMos voor LEDSTRIP

print("Start setup")
ledStrip = machine.Pin( PIN_LEDSTRIP, machine.Pin.OUT )
ultrasonic = HCSR04(trigger_pin=PIN_TRIGGER, echo_pin=PIN_ECHO, echo_timeout_us=1000000)
sun = ActualSunRise(WIFI_SSID, WIFI_PASSWORD)
print("Finished Setup")

# Continually try to connect to WiFi access point
while sun.connected():
    sunInfo = sun.info()
    distance = ultrasonic.distance_cm()
    print('Distance:', distance, 'cm', '| sunInfo =', sunInfo)
    
    if distance <= MAX_DISTANCE and sunInfo[1]:
        ledStrip.on()
    else:
        ledStrip.off()
    time.sleep_ms(SLEEP)
        
