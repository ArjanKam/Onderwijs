from machine import Pin
import time

relay = Pin(16, Pin.OUT) #relais op pin 16

while True:    
    relay.value(0)     # Relais uit
    print("Relay off")
    
    time.sleep(1)
    
    relay.value(1) 	  # Ralais aam
    print("Relay on") 
    time.sleep(1)