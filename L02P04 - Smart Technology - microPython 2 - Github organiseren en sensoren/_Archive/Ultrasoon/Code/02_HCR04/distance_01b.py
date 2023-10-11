from hcsr04 import HCSR04
from time import sleep

_sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)

def distance():
    return _sensor.distance_cm()

if __name__ == "__main__":
    while True:
        print('Distance:', distance(), 'cm')
        sleep(1)
