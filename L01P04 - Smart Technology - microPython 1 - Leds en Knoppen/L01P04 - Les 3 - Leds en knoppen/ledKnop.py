from machine import Pin
from time import sleep
print("knoppen en leds")

led01 = Pin(11, Pin.OUT)
led02 = Pin(12, Pin.OUT)
led03 = Pin(13, Pin.OUT)
knop01 = Pin(16, Pin.IN)
knop02 = Pin(17, Pin.IN)

counter = 0
while True:
    k1 = knop01.value() == 1
    k2 = knop02.value() == 1
    if k1:
        counter += 1
    if k2:
        counter -= 1
    print(counter)
    if counter == 0:
        led01.on()
        led02.off()
        led03.off()
    if counter == 1:
        led02.on()
        led01.off()
        led03.off()
    if counter == 2:
        led03.on()
        led01.off()
        led02.off()

 