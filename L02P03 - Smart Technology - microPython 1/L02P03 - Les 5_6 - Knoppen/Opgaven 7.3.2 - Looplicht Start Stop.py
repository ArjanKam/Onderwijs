from machine import Pin
from time import sleep

knop_blauw = Pin(28, Pin.IN)
   
PINNEN = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

pin = []
for id in PINNEN:
    pin.append(Pin(id, Pin.OUT))

id = 0
while True:
    pin[id].on()
    sleep(0.2)
    if knop_blauw.value() == 1:
        pin[id].off()
        sleep(0.2)
        id = id + 1
        if id >= len(pin):
            id = 0
            
            
