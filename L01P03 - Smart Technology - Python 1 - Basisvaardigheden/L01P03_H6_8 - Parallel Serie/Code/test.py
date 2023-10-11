from machine import Pin
import time

D = (16, 5, 4, 0, 2, 14, 12, 13, 15)

pinnen = []
for d in D:
    newPin = Pin(d, Pin.OUT)
    pinnen.append(newPin)

for pin in pinnen:
    pin.off()


