from machine import Pin
import time

PIN_D0 = 16
PIN_D1 = 5
PIN_D2 = 4
PIN_D3 = 0
PIN_D4 = 2
PIN_D5 = 14
PIN_D6 = 12
PIN_D7 = 13
PIN_D8 = 15

led0 = Pin(PIN_D0, Pin.OUT)
led1 = Pin(PIN_D1, Pin.OUT)
led2 = Pin(PIN_D2, Pin.OUT)
led3 = Pin(PIN_D3, Pin.OUT)
led4 = Pin(PIN_D4, Pin.OUT)
led5 = Pin(PIN_D5, Pin.OUT)
led6 = Pin(PIN_D6, Pin.OUT)
led7 = Pin(PIN_D7, Pin.OUT)
led8 = Pin(PIN_D8, Pin.OUT)

leds = (led0, led1, led2, led3, led4, led5, led6, led7, led8)

while True:
    for led in leds:
        led.on() 
        time.sleep(0.5)
    for led in leds:
        led.off()
        time.sleep(0.5)
    for pos in range(5):
        leds[pos].on()
        leds[8-pos].on()
        time.sleep(0.5)
    for led in leds:
        led.off()
        time.sleep(0.5)