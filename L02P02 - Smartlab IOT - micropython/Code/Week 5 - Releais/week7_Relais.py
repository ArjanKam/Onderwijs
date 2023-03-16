from machine import Pin
import time

SLEEP  = 1
PIN_D8 = 15

relais = Pin( PIN_D8, Pin.OUT)

while True:
    relais.on()
    time.sleep( SLEEP )
    relais.off()
    time.sleep( SLEEP )
            

