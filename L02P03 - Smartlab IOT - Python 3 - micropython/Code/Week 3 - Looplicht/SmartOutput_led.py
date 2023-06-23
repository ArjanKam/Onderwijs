from machine import Pin

LED_D0      = 16
LED_D1      = 5
LED_D2      = 4
LED_D3      = 0
LED_D4      = 2
LED_D5      = 14
LED_D6      = 12
LED_D7      = 13
LED_D8      = 15

led_d0 = Pin(LED_D0, Pin.OUT)
led_d1 = Pin(LED_D1, Pin.OUT)
led_d2 = Pin(LED_D2, Pin.OUT)
led_d3 = Pin(LED_D3, Pin.OUT)
led_d4 = Pin(LED_D4, Pin.OUT)
led_d5 = Pin(LED_D5, Pin.OUT)
led_d6 = Pin(LED_D6, Pin.OUT)
led_d7 = Pin(LED_D7, Pin.OUT)
led_d8 = Pin(LED_D8, Pin.OUT)

# led is een instatie van Pin(..)
#status is datatype Boolean of de led on=True of off(False) moet zijn
def setLed(led, status):
    if status:
        led.On()
    else:
        led.Off()
        
#d0..d8 zijn van het dataType boolean
def showResult(d0, d1, d2, d3, d4, d5, d6, d7, d8):
    setLed(led_d0, d0)
    setLed(led_d1, d1)
    setLed(led_d2, d2)
    setLed(led_d3, d3)
    setLed(led_d4, d4)
    setLed(led_d5, d5)
    setLed(led_d6, d6)
    setLed(led_d7, d7)
    setLed(led_d8, d8)

