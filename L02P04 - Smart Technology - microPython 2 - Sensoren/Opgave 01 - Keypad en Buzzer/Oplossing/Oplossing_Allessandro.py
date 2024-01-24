# Matrix Keypad
# NerdCave - https://www.youtube.com/channel/UCxxs1zIA4cDEBZAHIJ80NVg

from machine import Pin
from servo import *
import utime

# Create a map between keypad buttons and characters

matrix_keys = [['1', '2', '3'],
               ['4', '5', '6'],
               ['7', '8', '9'],
               ['*', '0', '#']]

NUMBER_OF_ROWS = 4
NUMBER_OF_COLUMNS = 3

# Define the GPIO pins on the pico
# corresponding with the pins on the Keypad
keypad_rows = [2,3,4,5]  # [R1, R2, R3, R4]
keypad_columns = [6,7,8] # [C1, C2, C3]

guess = []              # the keys entered by the user
secret_pin = ['1','2']  # our secret pincode

buzzer = Pin(15, Pin.OUT, Pin.PULL_UP)  # setup pin to be an output
servo = Servo(pin=28)
servo.rotateDeg(0)

row_pins = []
for pin in keypad_rows:
    row = Pin(pin, Pin.OUT)
    row.value(1)
    row_pins.append(row)
    
col_pins = []
for pin in keypad_columns:
    col_pins.append(Pin(pin, Pin.IN, Pin.PULL_DOWN))
    
##############################Scan keys ####################
    
def scankeys():
    for row in range(NUMBER_OF_ROWS):
        row_pins[row].high()
        for col in range(NUMBER_OF_COLUMNS): 
            if col_pins[col].value() == 1:
                key_press = matrix_keys[row][col]
                guess.append(key_press)
                print("You have pressed:", key_press)                
                utime.sleep(0.3)

            if len(guess) == len(secret_pin):
                checkPin(guess)  
        row_pins[row].low()
    
##############################To check Pin #################
def checkPin(guess):      
    if guess == secret_pin:
        print("You got the secret pin correct")
        for pos in range(0,180, 170):
            print(pos)
            servo.rotateDeg(pos)
            sleep(1)
        for pos in range(180,0, -170):
            print(pos)
            servo.rotateDeg(pos)
            sleep(1)
    else:
        print("Better luck next time")     
        buzzer.value(1)
        utime.sleep(2)
        buzzer.value(0)
        
    guess.clear()
    print("Enter the secret Pin")
    
###########################################################
    
print("Enter the secret Pin")
while True:
    
    scankeys()
    
   
            

           
