from machine import Pin
import time

SLEEP = 1       # 1 seconden
ONBOARD_LED = 2 # Led on WeMos

led = Pin( ONBOARD_LED, Pin.OUT )

while True:
    led.off()
    time.sleep( SLEEP )
    led.on()
    time.sleep( SLEEP )
    
    
    