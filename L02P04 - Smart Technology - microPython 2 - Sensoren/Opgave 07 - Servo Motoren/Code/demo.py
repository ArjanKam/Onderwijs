from machine import I2C, Pin
from servo import Servos

servo = Servos(i2c=I2C(id=0, sda=Pin(0), scl=Pin(1)), address=0x41)
servo.position(index=0, degrees=180)