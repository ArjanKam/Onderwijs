from machine import Pin
import time

SLEEP = 0.3
LED_D0 = 16
LED_D1 = 5
LED_D2 = 4
LED_D3 = 0
LED_D4 = 2 # Also inverse OnBoard
LED_D5 = 14
LED_D6 = 12
LED_D7 = 13
LED_D8 = 15

led0 = Pin( LED_D0, Pin.OUT)
led1 = Pin( LED_D1, Pin.OUT)
led2 = Pin( LED_D2, Pin.OUT)
led3 = Pin( LED_D3, Pin.OUT)
led4 = Pin( LED_D4, Pin.OUT)
led5 = Pin( LED_D5, Pin.OUT)
led6 = Pin( LED_D6, Pin.OUT)
led7 = Pin( LED_D7, Pin.OUT)
led8 = Pin( LED_D8, Pin.OUT)

led0.off()
led1.off()
led2.off()
led3.off()
led4.off()
led5.off()
led6.off()
led7.off()
led8.off()

while True:
    led0.on()
    time.sleep(SLEEP)
    led0.off()
    led1.on()
    time.sleep(SLEEP)
    led1.off()
    led2.on()
    time.sleep(SLEEP)
    
    
    