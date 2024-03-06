from time import sleep

teller1 = 0
teller2 = 0
teller3 = 0
TRUE_CHARACTERS = ("Y", "j", "y", "J")

def invoer(knopnummer):
    tekst = "Is knop " + str(knopnummer) + " ingedrukt ? : (j/n)"
    return input(tekst) in (TRUE_CHARACTERS)

def wcd1(aan):
    print("wcd1", aan)
    
def wcd2(aan):
    print("wcd2", aan)
    
def lamp1(aan):
    print("lamp1", aan)
    
def lamp2(aan):
    print("lamp2", aan)
    
def lamp3(aan):
    print("lamp3", aan)
    
def taak1():
    global teller1
    print("taak1")
    lamp1(True)
    if (teller1 % 3) != 0:
        lamp2(True)
        if (teller1 % 3) == 2:
            wcd1(True)
    teller1 += 1
    
def taak2():
    global teller2
    print("taak2")
    lamp3(True)
    teller2 += 1
    if (teller2 % 2) == 0:
        wcd2(True)
    
def taak3():
    global teller3
    print("taak3")
    lamp1(False)
    lamp2(False)
    lamp3(False)
    teller3 += 1
    if (teller3 % 2) == 0:
        wcd1 (False)
        wcd2 (False)

while True:
    knop1aan = invoer(1)
    knop2aan = invoer(2)
    knop3aan = invoer(3)

    if knop1aan:
        taak1()
    elif knop2aan:
        taak2()
    elif knop3aan:
        taak3()
    sleep(0.3)
