from machine import Pin
import time

#set constants
SLEEP = 0.1
PIN_D0 = 0  # standaard ....

PIN_D8 = 15 # standaard 0

#init global variables
knop = Pin( PIN_D8, Pin.IN)

# program
while True:
    time.sleep( SLEEP ) 
    print( knop.value() )
    