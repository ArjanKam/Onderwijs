from time import sleep
#import io_comp as io
import io_wemos as io

teller1 = 0
teller2 = 0
teller3 = 0

def taak1():
    print("taak1")
    io.lamp1(True)
    if (teller1 % 3) == 0:
        return
    
    io.lamp2(True)
    if (teller1 % 3) == 2:
        io.wcd1(True)
    
def taak2():
    print("taak2")
    io.lamp3(True)
    if (teller2 % 2) == 0:
        io.wcd2(True)
    
def taak3():
    print("taak3")
    io.lamp1(False)
    io.lamp2(False)
    io.lamp3(False)
    if (teller3 % 2) == 0:
        io.wcd1 (False)
        io.wcd2 (False)

while True:
    knop1aan = io.invoer(1)
    knop2aan = io.invoer(2)
    knop3aan = io.invoer(3)

    if knop1aan:
        teller1 += 1
        taak1()
    elif knop2aan:
        teller2 += 1
        taak2()
    elif knop3aan:
        teller3 += 1
        taak3()
    #
    sleep(0.3)
