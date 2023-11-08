from machine import Pin
import time
import ULTRASONE_HC_SR04 as hcsr04

SLEEP       = 1000 # 1 seconden
PIN_D = (16, 5, 4, 0, 2, 14, 12, 13, 15 )

ultrasonic = hcsr04.HCSR04(trigger_pin=PIN_D[7], echo_pin=PIN_D[6],
                           echo_timeout_us=1000000)

while True:
    distance = ultrasonic.distance_cm()
    print('Distance:', distance, 'cm', '|')
    
    time.sleep_ms(SLEEP)

