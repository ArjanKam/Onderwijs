from machine import Pin
from servo import *
import utime

led = Pin(25, Pin.OUT)
Buzzer = Pin(7, Pin.OUT)
keypad_rows = [3,4,5,6]
keypad_columns = [0,1,2]
piston = Pin(8, Pin.OUT)
servo = Servo(pin_id=9)


STATUS_NOT_COMPLETED = 0
STATUS_OK = 1
STATUS_FAIL = 2
piston.off()
matrix_keys = [['1', '2', '3'],
               ['4', '5', '6'],
               ['7', '8', '9'],
               ['*', '0', '#']]

guess = []
secret_pin = ["1","2","3"]

col_pins = []
row_pins = []
for x in range(0,len(keypad_rows)):
    row_pins.append(Pin(keypad_rows[x], Pin.OUT))
    row_pins[x].value(1)
    
for x in range(0,len(keypad_columns)):
    col_pins.append(Pin(keypad_columns[x], Pin.IN, Pin.PULL_DOWN))
    col_pins[x].value(0)
    
print("Please enter a key from the keypad")


def set_servo_angle(angle):
    
    duty_cycle = int((angle / 180.0) * 65535)
    servo_pwm.duty_u16(duty_cycle)
    utime.sleep(1)
    
def unlock():
    print("Unlocked")
    led.on()
    piston.on()
    servo.write(90)
    utime.sleep(5)
    servo.write(0)
    piston.off()
    led.off()

def lock():
    print("Wrong")
    Buzzer.on()
    utime.sleep(2)
    Buzzer.off()
    servo.write(0)

def scankeys():  
    for row in range(len(keypad_rows)):
        for col in range(len(keypad_columns)):
            row_pins[row].high()
            key = None
            
            if col_pins[col].value() == 1:
                print("You have pressed:", matrix_keys[row][col])
                key_press = matrix_keys[row][col]
                utime.sleep(0.3)
                guess.append(key_press)
        row_pins[row].low()

def checkCode():
    global guess
    if len(guess) != len(secret_pin):
        return STATUS_NOT_COMPLETED
    if guess == secret_pin:
        result = 1
    else:
        result = 2
    guess = []
    return result

while True:
    scankeys()
    status = checkCode()
    if status == 1:
        unlock()
    elif status == 2:
        lock()