from machine
import time
import ULTRASONE_HC_SR04 as hcsr04

SLEEP       = 1000 # 1 seconden
PIN_ECHO    = 0    # Pin van dre Echo -- Wijzigen
PIN_TRIGGER = 1    # PIN van de trigger -- Wijzigen
LED_STRIP   = 16   # GPIO16 on WeMos voor LEDSTRIP

ledStrip = machine.Pin( LED_STRIP, machine.Pin.OUT )
ultrasonic = hcsr04.HCSR04(trigger_pin=PIN_TRIGGER, echo_pin=PIN_ECHO,
                           echo_timeout_us=1000000)

while True:
    distance = ultrasonic.distance_cm()
    print('Distance:', distance, 'cm', '|')
    
    #indien afstand < 100 Dan LEDSTRIP aan, Ander UIT
    #Gebruik een costante voor de afstand
    ledStrip.on()
    ledStrip.off()
    
    time.sleep_ms(SLEEP)
