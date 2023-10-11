from machine import Pin

PINNEN = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

led = []
for pin in PINNEN:
    led.append( Pin(pin, Pin.OUT))

for l in led:
    l.off()
    
for l in led:
    l.on()
    time.sleep(0.3)
    l.off()
    
    
        
        