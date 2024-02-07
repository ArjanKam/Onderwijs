import machine
import time

SLEEP   = 2
LED     = 0 # Led GP0

led = machine.Pin(INTERNAL_LED, machine.Pin.OUT)

while True:
    led.on()
    time.sleep( SLEEP )
    led.off()
    time.sleep( SLEEP )
    
    
