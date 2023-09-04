from machine import Pin
import time

SLEEP = 0.3
PIN_D = (16, 5, 4, 0, 2, 14, 12, 13, 15 )

leds = []
for pin in PIN_D:
    newPin = Pin( pin, Pin.OUT)
    leds.append(newPin)
    newPin.off()

while True:
    for led in leds:
        led.on()
        time.sleep(SLEEP)
        led.off()
