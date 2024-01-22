# Copy with the filename : main.py on the pico.
# This 
import machine
from machine import I2C, Pin
import time
import uos
from random import random

led = Pin(25, Pin.OUT)
# need this UART to read from BME and be able to send data to local computer
uart = machine.UART(0, baudrate=115200)
uart.init(115200, bits=8, parity=None, stop=1, tx=Pin(0), rx=Pin(1))
#uos.dupterm(uart)
angle = 0
STEP = 1 
while True:
    #angleInput = uart.read()
    
    print('{:3};{:2};{:.2f}'.format(angle%360, STEP, random() * 200))
    #time.sleep(.2)
    led.toggle()
    angle += STEP
