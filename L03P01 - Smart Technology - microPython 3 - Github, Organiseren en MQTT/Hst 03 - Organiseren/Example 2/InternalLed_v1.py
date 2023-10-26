from machine import Pin
import utime
#use unstable firmware of the w-version !!!!
PIN_INTERNAL_LED = "LED" #25 -> on W this is not working
led = Pin(PIN_INTERNAL_LED, Pin.OUT)

while True:
    led.on()
    utime.sleep(1)
    led.off()
    utime.sleep(1)