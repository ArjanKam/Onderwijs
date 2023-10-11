from machine import Pin
import time
import ULTRASONE_HC_SR04 as hcsr04

SLEEP       = 1000 # 1 seconden
PIN_D = (16, 5, 4, 0, 2, 14, 12, 13, 15 )
PIN_ECHO    = PIN_D[???]    # Pin van de Echo -- Wijzigen
PIN_TRIGGER = PIN_D[???]    # PIN van de trigger -- Wijzigen

ledHoog = Pin( PIN_D[0], Pin.OUT )
ledLaag = Pin( PIN_D[1], Pin.OUT )
ultrasonic = hcsr04.HCSR04(trigger_pin=PIN_TRIGGER, echo_pin=PIN_ECHO,
                           echo_timeout_us=1000000)

while True:
    distance = ultrasonic.distance_cm()
    print('Distance:', distance, 'cm', '|')
    
    time.sleep_ms(SLEEP)

