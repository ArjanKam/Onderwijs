from machine import Pin
import time

SLEEP  = 2
LED_D4 = 2

led4 = Pin( LED_D4, Pin.OUT)

led4.on()
time.sleep( SLEEP )
led4.off()
time.sleep( SLEEP )
        

