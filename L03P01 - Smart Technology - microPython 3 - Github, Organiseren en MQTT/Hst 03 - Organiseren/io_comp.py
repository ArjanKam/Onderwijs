_TRUE_CHARACTERS = ("Y", "j", "y", "J")

def invoer(knopnummer):
    tekst = "Is knop " + str(knopnummer) + " ingedrukt ? : (j/n)"
    return input(tekst) in (_TRUE_CHARACTERS)

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
    
if __name__ == "__main__":
    invoer(1)
    invoer(2)
    invoer(3)
    wcd1(True)
    wcd1(False)
    wcd2(True)
    wcd2(False)
    lamp1(True)
    lamp1(False)
    lamp2(True)
    lamp2(False)
    lamp3(True)
    lamp3(False)