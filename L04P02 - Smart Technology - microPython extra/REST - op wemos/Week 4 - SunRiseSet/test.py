from machine import Pin
import time

LED_D4 = 15

led4 = Pin(LED_D4, Pin.OUT)

while True:
    led4.on()
    time.sleep(1)
    led4.off()
    time.sleep(1)