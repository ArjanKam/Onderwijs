from pca9685 import PCA9685
from machine import I2C, Pin
from servo import Servos

i2c = I2C(id=0, sda=Pin(0), scl=Pin(1))

pca = PCA9685(i2c=i2c)
servo = Servos(i2c=i2c)
servo.position(index=0, degrees=180)