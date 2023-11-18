from machine import Pin
from dil import *

pin01 = Pin(1, Pin.IN)
pin02 = Pin(2, Pin.IN)
pin03 = Pin(3, Pin.OUT)

pin04 = Pin(4, Pin.IN)
pin05 = Pin(5, Pin.IN)
pin06 = Pin(6, Pin.OUT)

pin13 = Pin(7, Pin.IN)
pin12 = Pin(8, Pin.IN)
pin11 = Pin(9, Pin.OUT)

pin10 = Pin(10, Pin.IN)
pin09 = Pin(11, Pin.IN)
pin08 = Pin(12, Pin.OUT)
pinSet1 = (pin01, pin02, pin03)
pinSet2 = (pin04, pin05, pin06)
pinSet3 = (pin13, pin12, pin11)
pinSet4 = (pin10, pin09, pin08)

Dil().print()
Dil(pinSet1, pinSet2, pinSet3, pinSet4, debugResult=RESULT_AND).print()
Dil(pinSet1, pinSet2, pinSet3, pinSet4, debugResult=RESULT_OR).print()
Dil(pinSet1, pinSet2, pinSet3, pinSet4, debugResult=RESULT_XOR).print()
Dil(pinSet1, pinSet2, pinSet3, pinSet4, debugResult=RESULT_NAND).print()
Dil(pinSet1, pinSet2, pinSet3, pinSet4, debugResult=RESULT_NOR).print()
Dil(pinSet1, pinSet2, pinSet3, pinSet4, debugResult=RESULT_NXOR).print()
Dil(pinSet1, pinSet2, pinSet3, pinSet4, debugResult=ERROR).print()


