import ADS1115 as AD
from machine import Pin, SoftI2C
import math

PIN_D = (16, 5, 4, 0, 2, 14, 12, 13, 15)
MAX_MEASURE_VALUE = 30500
i2c = SoftI2C(scl=Pin(PIN_D[1]), sda=Pin(PIN_D[2]))
ad = AD.ADS1115(i2c)

def getMeasurentDemo(X, width, height):
    rad = (3* X / (width)) * math.pi
    y = (height//2) * (1 + math.sin(rad))
    return int(y)

def getMeasurement(width, height, pin=0):
    waarde = ad.read(3, pin)
    if waarde < 0:
        waarde = 0
    y = height * waarde / MAX_MEASURE_VALUE
    return int(y), waarde
