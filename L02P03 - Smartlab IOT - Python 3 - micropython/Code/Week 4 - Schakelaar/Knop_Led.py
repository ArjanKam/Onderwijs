# demo voor gebruik van Knop
from machine import Pin

PIN_KNOP = 16 # Aansluiting op D0
LED_D4   = 2  # Also Onboard LED

knop = Pin( PIN_KNOP, Pin.IN)
led4 = Pin( LED_D4, Pin.OUT)

while True:
    if knop.value() == True:
        print("Hoog")
        led4.on()
    else:
        led4.off()
    