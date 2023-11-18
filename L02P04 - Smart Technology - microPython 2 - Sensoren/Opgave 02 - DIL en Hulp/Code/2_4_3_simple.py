from machine import Pin

CHECK       = ((0,0),(0,1),(1,0),(1,1))
RESULT_NAND  = (1,1,1,0)

pin01 = Pin(1, Pin.IN)
pin02 = Pin(2, Pin.IN)
pin03 = Pin(3, Pin.OUT)

#pinA and pinB are of type Pin.IN
#pinOut is of type Pin.OUT
#if the pins are set according to the CHECK we check if
#pinOUT is of the NAND logic
def isNand(pinA: Pin, pinB: Pin, pinOut: Pin) -> bool:
    for index, check in enumerate(CHECK):
        pinA.value = check[0]
        pinB.value = check[1]        
        if pinOut.value() != RESULT_NAND[index]:
            return False
    return True

print( isNand(pin01, pin02, pin03) )

