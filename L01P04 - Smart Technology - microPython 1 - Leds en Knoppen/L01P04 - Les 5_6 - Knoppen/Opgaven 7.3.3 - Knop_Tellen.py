#import libraries
from machine import Pin
import time

#set constants
SLEEP = 0.1

PIN = 0 

#init global variables
knop = Pin( PIN, Pin.IN)
teller = 0

# program
while True:
    time.sleep( SLEEP ) 
    print( teller, knop.value() )
    teller = teller + 1 
    