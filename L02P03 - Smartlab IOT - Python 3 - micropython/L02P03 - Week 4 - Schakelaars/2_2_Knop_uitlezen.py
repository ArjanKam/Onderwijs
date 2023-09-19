from machine import Pin
import time

#set constants
SLEEP = 0.1
PIN_8 = 15

#init global variables
knop = Pin( PIN_8, Pin.IN)

# program
while True:
    time.sleep( SLEEP ) 
    print( knop.value() )
    