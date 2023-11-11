import machine
from time import sleep

class Servo:
    def __init__(self, MIN_DUTY=300000, MAX_DUTY=2300000, pin=0, freq=50):
        self.pwm = machine.PWM(machine.Pin(pin))
        self.pwm.freq(freq)
        self.MIN_DUTY = MIN_DUTY
        self.MAX_DUTY = MAX_DUTY
        
    def rotateDeg(self, deg):
        deg = max(0, min(deg, 180))
        duty_ns = int(self.MAX_DUTY - deg * (self.MAX_DUTY-self.MIN_DUTY)/180)
        self.pwm.duty_ns(duty_ns)

servo = Servo(pin=28)
servo.rotateDeg(90)
while False:
    for pos in range(0,180, 5):
        print(pos)
        servo.rotateDeg(pos)
        sleep(1)
    for pos in range(180,0, -5):
        print(pos)
        servo.rotateDeg(pos)
        sleep(1)
