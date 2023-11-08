import machine
import time
from ULTRASONE_HC_SR04 import HCSR04

MAX_DISTANCE= 100  # 
SLEEP       = 1000 # 1 seconden
PIN_ECHO    = 4    # Pin van dre Echo
PIN_TRIGGER = 5    # PIN van de trigger
PIN_LEDSTRIP= 16   # GPIO16 on WeMos voor LEDSTRIP

print("Setup Wemos")
ledStrip = machine.Pin( PIN_LEDSTRIP, machine.Pin.OUT )
ultrasonic = HCSR04(trigger_pin=PIN_TRIGGER, echo_pin=PIN_ECHO, echo_timeout_us=1000000)
print("Finished Setup")

# Run code
while True:
    distance = ultrasonic.distance_cm()
    print('Distance:', distance, 'cm', '|')
    if distance <= MAX_DISTANCE:
        ledStrip.on()
    else:
        ledStrip.off()
    time.sleep_ms(SLEEP)
