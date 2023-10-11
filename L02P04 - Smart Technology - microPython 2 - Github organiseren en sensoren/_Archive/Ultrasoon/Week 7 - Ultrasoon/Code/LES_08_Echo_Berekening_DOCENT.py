from machine import Pin
import time
import ULTRASONE_HC_SR04 as hcsr04
 
SLEEP       = 1000 # 1 seconden
PIN_D       = (16, 5, 4, 0, 2, 14, 12, 13, 15 )
PIN_ECHO    = PIN_D[7]    # Pin 7 van de Echo 
PIN_TRIGGER = PIN_D[6]    # PIN 6 van de trigger
AFSTAND_LED = 20
ledHoog = Pin( PIN_D[0], Pin.OUT )
ledLaag = Pin( PIN_D[1], Pin.OUT )
ultrasonic = hcsr04.HCSR04(trigger_pin=PIN_TRIGGER, echo_pin=PIN_ECHO,
                           echo_timeout_us=1000000)
while True:
    distance = ultrasonic.distance_cm()
    print('Distance:', distance, 'cm', '|')
    
    if distance > AFSTAND_LED:
        ledHoog.on()
        ledLaag.off()
    else:
        ledHoog.off()
        ledLaag.on()
    time.sleep_ms(SLEEP)

