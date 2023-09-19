# demo voor gebruik van Knop

#import libraries
from machine import Pin
import time

#set constants
SLEEP = 0.1

PIN_PULLDOWN0 = 16 # Aansluiting op D0
PIN_PULLDOWN1 =  5 # Aansluiting op D1
PIN_PULLDOWN2 =  4 # Aansluiting op D2
PIN_PULLDOWN6   = 12 # Aansluiting op D6 -- Blijft op waarde zonder pin !!!
PIN_PULLDOWN8 = 15 # Aansluiting op D8

PIN_PULLUPP3   =  0 # Aansluiting op D3
PIN_PULLUPP4   =  2 # Aansluiting op D4
PIN_PULLUPP5   = 14 # Aansluiting op D5
PIN_PULLUPP7   = 13 # Aansluiting op D7

#init global variables
knop = Pin( PIN_PULLDOWN6, Pin.IN)
teller = 0

# program
while True:
    time.sleep( SLEEP ) 
    print( teller, knop.value() )
    teller = teller + 1 
    