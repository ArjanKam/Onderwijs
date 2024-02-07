from machine import Pin

PINNEN = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
led = []
for pin in PINNEN:
    led.append( Pin(pin, Pin.OUT))

# all leds in list led will be turned off
def allLedsOff():
    for l in led:
        l.off()
        
#turn led on, sleep(time), turn led off        
def ledOnOff(led, time):
    led.on()
    time.sleep(time)
    led.off()

#main program
for l in led:
    ledOnOff(l, 0.3)
    
    
        
        