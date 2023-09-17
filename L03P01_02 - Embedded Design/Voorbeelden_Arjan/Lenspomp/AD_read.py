import ADS1115 as AD
from machine import Pin, SoftI2C
import time
PIN_D = (16, 5, 4, 0, 2, 14, 12, 13, 15)

i2c = SoftI2C(scl=Pin(PIN_D[1]), sda=Pin(PIN_D[2]))
ad = AD.ADS1115(i2c)

while True:
    print(ad.read(3, 0))
    time.sleep(0.5)