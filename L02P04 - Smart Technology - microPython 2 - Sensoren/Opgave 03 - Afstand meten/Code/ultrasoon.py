from machine import Pin
from hcrs04 import HCSR04
from time import sleep

SLEEP       = 1
TRIGGER_PIN = 21
PIN_ECHO    = 20

_sensor = HCSR04(trigger_pin=TRIGGER_PIN, echo_pin=PIN_ECHO, echo_timeout_us=10000)

def measure():
    return _sensor.distance_cm()

if __name__ == "__main__":
    while True:
        print('Distance:', measure(), 'cm', '|')
        time.sleep(SLEEP)

