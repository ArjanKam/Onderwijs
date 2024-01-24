from machine import Pin,PWM
from time import sleep
 
INA = 14
INB = 15

ina_pin = Pin(INA, Pin.OUT)
inb_pin = Pin(INB, Pin.OUT)

while True:
    try:
        user_input = int(input('Voer in:0 cw \n 	1 ccw \n 	2 stop \ntype: '))

        if user_input == 1:
            ina_pin.value(0)
            inb_pin.value(0)
            sleep(0.2)
            ina_pin.value(1)
            inb_pin.value(0)
            
        elif user_input == 0:
            ina_pin.value(0)
            inb_pin.value(0)
            sleep(0.2)
            ina_pin.value(0)
            inb_pin.value(1)
            
        elif user_input == 2:
            ina_pin.value(0)
            inb_pin.value(0)        
            break
    
    except ValueError:
        ina_pin.value(0)
        inb_pin.value(0)