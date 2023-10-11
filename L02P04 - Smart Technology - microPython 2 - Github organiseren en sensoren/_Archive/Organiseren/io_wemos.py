from machine import Pin
from time import sleep

_PIN_D       = (16, 5, 4 , 0, 2, 14, 12, 13, 15)

_pinWCD1    = Pin( _PIN_D[0], Pin.OUT)
_pinWCD2    = Pin( _PIN_D[1], Pin.OUT)
_pinLamp1   = Pin( _PIN_D[2], Pin.OUT)
_pinLamp2   = Pin( _PIN_D[3], Pin.OUT)
_pinLamp3   = Pin( _PIN_D[4], Pin.OUT)

_drukknop1  = Pin( _PIN_D[5], Pin.IN)
_drukknop2  = Pin( _PIN_D[6], Pin.IN)
_drukknop3  = Pin( _PIN_D[7], Pin.IN)

def _alles(aan):
    for pin in _PIN_D:
        if aan:
            Pin( pin, Pin.OUT).on()
        else:
            Pin( pin, Pin.OUT).off()
            
def invoer(knopnummer):
    if knopnummer == 1:
        return _drukknop1.value() == 1
    if knopnummer == 2:
        return _drukknop2.value() == 1
    if knopnummer == 3:
        return _drukknop3.value() == 1
    return False

def wcd1(aan):
    if aan:
        _pinWCD1.on()
    else:
        _pinWCD1.off()
        
def wcd2(aan):
    if aan:
        _pinWCD2.on()
    else:
        _pinWCD2.off()
    
def lamp1(aan):
    if aan:
        _pinLamp1.on()
    else:
        _pinLamp1.off()
        
def lamp2(aan):
    if aan:
        _pinLamp2.on()
    else:
        _pinLamp2.off()
        
def lamp3(aan):
    if aan:
        _pinLamp3.on()
    else:
        _pinLamp3.off()

_alles(False)
if __name__ == "__main__":
    print("Alle leds zijn nu AAN")
    _alles(True)
    sleep(1)
    print("Alle leds zijn nu UIT")
    _alles(False)
    
    input("Druk op de knop 1 en tegelijk op <enter>")
    print("Status knop 1 = ", invoer(1))
    input("Druk NIET op de knop 1 en tegelijk op <enter>")
    print("Status knop 1 = ", invoer(1))
    
    input("Druk op de knop 2 en tegelijk op <enter>")
    print("Status knop 2 = ", invoer(2))
    input("Druk NIET op de knop 2 en tegelijk op <enter>")
    print("Status knop 1 = ", invoer(2))
    
    input("Druk op de knop 3 en tegelijk op <enter>")
    print("Status knop 3 = ", invoer(3))
    input("Druk NIET op de knop 3 en tegelijk op <enter>")
    print("Status knop 3 = ", invoer(3))
    
    lamp1(True)
    sleep(1)
    lamp1(False)
    sleep(1)
    
    lamp2(True)
    sleep(1)
    lamp2(False)
    sleep(1)
    
    lamp3(True)
    sleep(1)
    lamp3(False)
    sleep(1)
    
    wcd1(True)
    sleep(1)
    wcd1(False)
    sleep(1)
    
    wcd2(True)
    sleep(1)
    wcd2(False)
    sleep(1)
    