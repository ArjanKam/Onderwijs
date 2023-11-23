from machine import Pin
from time import sleep

CHECK       = ((0,0),(0,1),(1,0),(1,1))
RESULT_NAND  = (1,1,1,0)
RESULT_OR    = (0,1,1,1)  
pin01 = Pin(1, Pin.OUT)
pin02 = Pin(2, Pin.IN)
pin03 = Pin(3, Pin.OUT)

def isNand(pinA: Pin, pinB: Pin, pinOut: Pin, test = None) -> bool:
    for index, check in enumerate(CHECK):
        pinA.value = check[0]
        pinB.value = check[1]
        if test != None:
            pinOut._value = test[index]
        if pinOut.value() != RESULT_NAND[index]:
            return False
    return True

print( isNand(pin01, pin02, pin03, RESULT_NAND) )
