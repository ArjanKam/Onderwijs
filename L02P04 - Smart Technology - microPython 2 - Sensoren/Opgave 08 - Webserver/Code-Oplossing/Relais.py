from machine import Pin
from time import *

relay = Pin(16, Pin.OUT) #relais op pin 16

while True:
    relay.value(0) # Relais uit
    print("Relay off")
    
    sleep(5)
    
    relay.value(1) # Relais aan
    print("Relay on")
    sleep(5)