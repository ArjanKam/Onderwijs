import math

teller = 0
def getMeasurement(width, height):
    global teller
    rad = (3* teller / (width)) * math.pi
    y = (height//2) * (1 + math.sin(rad))
    
    teller += 1
    return int(y)