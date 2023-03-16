from machine import Pin
import time

#LED_D0 = 16
LED_D1 = 5
LED_D2 = 4
LED_D3 = 0
LED_D4 = 2 # Also inverse OnBoard
LED_D5 = 14
LED_D6 = 12
LED_D7 = 13
#LED_D8 = 15

KNOP_DOWN = 16    # op D0     # Standaard waarde
KNOP_UP = 15   # op D8     # Standaard waarde

#led0 = Pin( LED_D0, Pin.OUT)
led1 = Pin( LED_D1, Pin.OUT) #
led2 = Pin( LED_D2, Pin.OUT)
led3 = Pin( LED_D3, Pin.OUT)
led4 = Pin( LED_D4, Pin.OUT)
led5 = Pin( LED_D5, Pin.OUT)
led6 = Pin( LED_D6, Pin.OUT)
led7 = Pin( LED_D7, Pin.OUT)
#led8 = Pin( LED_D8, Pin.OUT)

knopUp   = Pin( KNOP_DOWN, Pin.IN)
knopDown = Pin( KNOP_UP, Pin.IN)

led1.off()
led2.off()
led3.off()
led4.on()
led5.off()
led6.off()
led7.off()
welkeLedAan = 4

while True:
    up = knopUp.value()
    down = knopDown.value()
    print(up, down)
    
    if up == 1 and down == 1:
        led1.off()
        led2.off()
        led3.off()
        led4.on()
        led5.off()
        led6.off()
        led7.off()
    else:
        if up == 1:
            welkeLedAan = welkeLedAan + 1
            print(welkeLedAan)
        elif down == 1:
            welkeLedAan = welkeLedAan - 1
            print(welkeLedAan)
            
            
            
    

