MORSE_TABEL = [
    ["A", [1, 2]],
    ["B", [2, 1, 1, 1]],
    ["C", [2, 1, 2, 1]],
    ["D", [2, 1, 1]],
    ["E", [1]],
    ["F", [1, 1, 2, 1]],
    ["G", [2, 2, 1]],
    ["H", [1, 1, 1, 1]],
    ["I", [1, 1]],
    ["J", [1, 2, 2, 2]],
    ["K", [2, 1, 2]],
    ["L", [1, 2, 1, 1]],
    ["M", [2, 2]],
    ["N", [2, 1]],
    ["O", [2, 2, 2]],
    ["P", [1, 2, 2, 1]],
    ["Q", [2, 2, 1, 2]],
    ["R", [1, 2, 1]],
    ["S", [1, 1, 1]],
    ["T", [2]],
    ["U", [1, 1, 2]],
    ["V", [1, 1, 1, 2]],
    ["W", [1, 2, 2]],
    ["X", [2, 1, 1, 2]],
    ["Y", [2, 1, 2, 2]],
    ["Z", [2, 2, 1, 1]],
]


TIME_LINE = 0.8
TIME_DOT = 0.4
TIME_BETWEEN = 0.2

from machine import Pin
from utime import sleep
#use unstable firmware of the w-version  !!!!
PIN_LED = 21
_led = Pin (PIN_LED, Pin.OUT)


def on(): #functie
    _led.on()
    
def off():
    _led.off()

def line():
    on()
    print("on")
    sleep(TIME_LINE)
    off()
    print("off")
    

def dot():
    on()
    print("on")
    sleep(TIME_DOT)
    off()
    print("off")
    
    

    
def morse2_led(x):
    for i in range(len(x)):
        print(x[i])
        if x[i] == 1:
            line()
            off()
            sleep(TIME_BETWEEN)
        
        elif x[i] == 2:
            dot()
            off()
            sleep(TIME_BETWEEN)
    
morse2_led(MORSE_TABEL[0][1])


    



    


    

