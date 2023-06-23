from machine import Pin
import time

SLEEP = .2
PIN_D0 = 16
PIN_D1 = 5
PIN_D2 = 4
PIN_D3 = 0
PIN_D4 = 2 # Also inverse OnBoard
PIN_D5 = 14
PIN_D6 = 12
PIN_D7 = 13
PIN_D8 = 15

knopLinks = Pin( PIN_D0, Pin.IN)
led1 = Pin( PIN_D1, Pin.OUT)
led2 = Pin( PIN_D2, Pin.OUT)
led3 = Pin( PIN_D3, Pin.OUT)
led4 = Pin( PIN_D4, Pin.OUT)
led5 = Pin( PIN_D5, Pin.OUT)
led6 = Pin( PIN_D6, Pin.OUT)
led7 = Pin( PIN_D7, Pin.OUT)
knopRechts = Pin( PIN_D8, Pin.IN)

led1.off()
led2.off()
led3.off()
led4.on()
led5.off()
led6.off()
led7.off()

huidigLedje = 4
while True:
    linksAan  = knopLinks.value()  == 1
    rechtsAan = knopRechts.value() == 1
    
    print("links", linksAan, "rechts", rechtsAan)
    time.sleep(SLEEP)
    if linksAan and rechtsAan:
        led1.off()
        led2.off()
        led3.off()
        led4.on()
        led5.off()
        led6.off()
        led7.off()
    else:
        if rechtsAan:
            if huidigLedje < 7:
                # huidige Led uit
                if huidigLedje == 1:
                    led1.off()
                    led2.on()
                elif huidigLedje == 2:
                    led2.off()
                    led3.on()
                elif huidigLedje == 3:
                    led3.off()
                    led4.on()
                elif huidigLedje == 4:
                    led4.off()
                    led5.on()
                elif huidigLedje == 5:
                    led5.off()
                    led6.on()
                elif huidigLedje == 6:
                    led6.off()
                    led7.on()
                huidigLedje = huidigLedje + 1
        elif linksAan:
            if huidigLedje > 1:
                # huidige Led uit
                if huidigLedje == 1:
                    led2.off()
                    led1.on()
                elif huidigLedje == 2:
                    led3.off()
                    led2.on()
                elif huidigLedje == 3:
                    led4.off()
                    led3.on()
                elif huidigLedje == 4:
                    led5.off()
                    led4.on()
                elif huidigLedje == 5:
                    led6.off()
                    led5.on()
                elif huidigLedje == 6:
                    led7.off()
                    led6.on()
                huidigLedje = huidigLedje - 1
    