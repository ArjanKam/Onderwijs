from machine import Pin
'''Dit systeem geeft als output alleen de DIL aan die het is, bv: XNOR'''

CHECK = ((0,0),(0,1),(1,0),(1,1))
RESULT_AND = (0,0,0,1)
RESULT_NAND = (1,1,1,0)
RESULT_OR = (0,1,1,1)
RESULT_NOR = (1,0,0,0)
RESULT_XOR = (0,1,1,0)
RESULT_XNOR = (1,0,0,1)

supportedPorts = {RESULT_AND: "AND",
                  RESULT_NAND: "NAND",
                  RESULT_OR : "OR",
                  RESULT_NOR : "NOR",
                  RESULT_XOR : "XOR",
                  RESULT_XNOR : "XNOR"
                  }

pin01 = Pin(7, Pin.OUT)
pin02 = Pin(6, Pin.OUT)
pin03 = Pin(5, Pin.IN)

pin04 = Pin(4, Pin.OUT)
pin05 = Pin(3, Pin.OUT)
pin06 = Pin(2, Pin.IN)

pin07 = Pin(21	, Pin.OUT)
pin08 = Pin(20, Pin.OUT)
pin09 = Pin(19, Pin.IN)

pin10 = Pin(18, Pin.OUT)
pin11 = Pin(17, Pin.OUT)
pin12 = Pin(16, Pin.IN)


def checklogical(pinA: Pin, pinB: Pin, pinOut: Pin) -> bool:
    result = []
    for check in CHECK:
        pinA.value(check[0])
        pinB.value(check[1])
        result.append(pinOut.value())
    return tuple(result)

def checkPort():
    result1 = checklogical(pin01, pin02, pin03)
    result2 = checklogical(pin04, pin05, pin06)
    result3 = checklogical(pin07, pin08, pin09)
    result4 = checklogical(pin10, pin11, pin12)

    #print(CHECK, "->", result1, result2, result3, result4)

    if result1 == result2 == result3 == result4 in supportedPorts:
        return supportedPorts[result1]
    else:
        return "Unknown"

_oldPort = None
while True:
    port = checkPort()
    if _oldPort != port:
        print(port)
        _oldPort = port