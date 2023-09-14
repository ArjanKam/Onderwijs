from machine import Pin
from time import sleep

pin = Pin(0, Pin.OUT)

while True:
    pin.on()
    sleep(1)
    pin.off()
    sleep(1)
    