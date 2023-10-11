from machine import Pin
from utime import sleep
#use unstable firmware of the w-version !!!!
PIN_INTERNAL_LED = "LED" #25 -> on W this is not working
_led = Pin(PIN_INTERNAL_LED, Pin.OUT)

_teller = 10
def _tienKeerKnipperen():
    while _teller > 0:
        _led.on()
        time.sleep(0.1)
        _led.off()
        time.sleep(0.1)
        _teller -= 1
    _teller = 10

def on():
    _led.on()
    
def off():
    _led.off()

print(__name__)
if __name__ == "__main__":
    while True:
        on()
        sleep(1)
        off()
        sleep(1)
