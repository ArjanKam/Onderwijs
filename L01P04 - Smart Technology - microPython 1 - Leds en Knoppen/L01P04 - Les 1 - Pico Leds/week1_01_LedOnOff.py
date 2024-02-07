import machine
import time

SLEEP  = 2
#INTERNAL_LED = 25   # pico-H 
INTERNAL_LED = "LED" # pico-W 

led = machine.Pin(INTERNAL_LED, machine.Pin.OUT)

aantalKnipperen = 10
while aantalKnipperen > 0:
    led.on()
    time.sleep( SLEEP )
    led.off()
    time.sleep( SLEEP )
    aantalKnipperen = aantalKnipperen - 1

