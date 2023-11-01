from machine import Pin
import time

SLEEP = 0.2
PIN_D0 = 16
PIN_D1 = 5
PIN_D2 = 4
PIN_D3 = 0
PIN_D4 = 2 # Also inverse OnBoard
PIN_D5 = 14
PIN_D6 = 12
PIN_D7 = 13
PIN_D8 = 15

knop0 = Pin( PIN_D0, Pin.IN)
led1 = Pin( PIN_D1, Pin.OUT)
led2 = Pin( PIN_D2, Pin.OUT)
led3 = Pin( PIN_D3, Pin.OUT)
led4 = Pin( PIN_D4, Pin.OUT)
led5 = Pin( PIN_D5, Pin.OUT)
led6 = Pin( PIN_D6, Pin.OUT)
led7 = Pin( PIN_D7, Pin.OUT)
knop8 = Pin( PIN_D8, Pin.IN)

led1.off()
led2.off()
led3.off()
led4.on()
led5.off()
led6.off()
led7.off()
welkeLedAan = 4

while True:
    waarde_0 = knop0.value()
    waarde_8 = knop8.value()
    print("knop0", waarde_0, "knop8", waarde_8, "LedAan", welkeLedAan)
    time.sleep(SLEEP)
    
    if waarde_0 == 1 and waarde_8 == 1:
        welkeLedAan = 4
    elif waarde_0 == 1:
        welkeLedAan = welkeLedAan - 1
    elif waarde_8 == 1:
        welkeLedAan = welkeLedAan + 1

    if welkeLedAan < 1:
        welkeLedAan = 1
    elif welkeLedAan > 7:
        welkeLedAan = 7
    
    if welkeLedAan == 1:
        led1.on()
        led2.off()
        led3.off()
        led4.off()
        led5.off()
        led6.off()
        led7.off()
    elif welkeLedAan == 2:
        led1.off()
        led2.on()
        led3.off()
        led4.off()
        led5.off()
        led6.off()
        led7.off()
    elif welkeLedAan == 3:
        led1.off()
        led2.off()
        led3.on()
        led4.off()
        led5.off()
        led6.off()
        led7.off()
    elif welkeLedAan == 4:
        led1.off()
        led2.off()
        led3.off()
        led4.on()
        led5.off()
        led6.off()
        led7.off()
    elif welkeLedAan == 5:
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        led5.on()
        led6.off()
        led7.off()
    elif welkeLedAan == 6:
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        led5.off()
        led6.on()
        led7.off()
    elif welkeLedAan == 7:
        led1.off()
        led2.off()
        led3.off()
        led4.off()
        led5.off()
        led6.off()
        led7.on()