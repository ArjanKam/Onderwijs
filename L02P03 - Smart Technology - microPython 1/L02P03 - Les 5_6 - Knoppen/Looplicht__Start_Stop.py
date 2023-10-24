from machine import Pin
from time import sleep

PINNEN = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

pin = []
for id in PINNEN:
    pin.append(Pin(id, Pin.OUT))

knop_blauw = Pin(28, Pin.IN)

teller = 0
while True:
    print(teller, knop_blauw.value())
    sleep(1)
    teller += 1
    
   
# for led in pin:
#     led.on()
#     sleep(0.2)
#     led.off()
#     sleep(0.2)
# 