from machine import Pin
import time

#set constants
SLEEP = 0.5
PIN_D0   = 16 # Standaard 0
PIN_D1   =  5 # Standaard 0
PIN_D2   =  4 # Standaard 0
PIN_D6   = 12 # Standaard 0 -- Blijft op waarde zonder pin !!!
PIN_D8   = 15 # Standaard 0

PIN_D3   =  0 # Standaard 1
PIN_D4   =  2 # Standaard 1
PIN_D5   = 14 # Standaard 1
PIN_D7   = 13 # Standaard 1

#init global variables
knop = Pin( PIN_D8, Pin.IN)

# program
while True:
    time.sleep( SLEEP ) 
    print( knop.value() )
    