from machine import Pin

CHECK       = ((0,0),(0,1),(1,0),(1,1))
RESULT_NAND  = (1,1,1,0)
RESULT_OR    = (0,1,1,1)
pin01 = Pin(1, Pin.OUT)
pin02 = Pin(2, Pin.OUT)
pin03 = Pin(3, Pin.IN)

#pinA and pinB are of type Pin.IN
#pinOut is of type Pin.OUT
#if the pins are set according to the CHECK we check if
#pinOUT behaves like the given logic
def checkLogical(pinA: Pin, pinB: Pin, pinOut: Pin, logic : tuple) -> bool:
    for index, check in enumerate(CHECK):
        pinA.value(check[0])
        pinB.value(check[1])
        if pinOut.value() != logic[index]:
            return False
    return True

print( checkLogical(pin01, pin02, pin03, RESULT_NAND) )
print( checkLogical(pin01, pin02, pin03, RESULT_OR) )

schakelaar = Pin(0, Pin.IN, Pin.PULL_UP)

