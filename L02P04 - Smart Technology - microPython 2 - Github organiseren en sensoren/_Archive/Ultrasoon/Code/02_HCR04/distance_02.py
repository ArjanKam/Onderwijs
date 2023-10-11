from hcsr04 import HCSR04

PIN_TRIGGER = 21
PIN_ECHO    = 20

_sensor = HCSR04(trigger_pin=PIN_TRIGGER, echo_pin=PIN_ECHO, echo_timeout_us=10000)

def measure()
    return _sensor.distance_cm()
    
if __name__ == "__main__":
    d = measure
    print('Distance:', d, 'cm')