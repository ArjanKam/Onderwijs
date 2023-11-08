from machine import Pin
import time

SLEEP = 1        # 1 seconden
ONBOARD_LED = 16 # GPIO16 on WeMos voor LEDSTRIP

led = Pin( ONBOARD_LED, Pin.OUT )
led1 = Pin( 12, Pin.OUT )
led2 = Pin( 13, Pin.OUT )
led3 = Pin( 14, Pin.OUT )
led4 = Pin( 15, Pin.OUT )

while True:
    led.off()
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    input("<<press enter to change state>>")
    led.on()
    led1.on()
    led2.on()
    led3.on()
    led4.on()
    input("<<press enter to change state>>")
    
    
    