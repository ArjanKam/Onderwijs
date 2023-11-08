from hcsr04 import HCSR04

PIN_TRIGGER_1 = 21
PIN_ECHO_1    = 20

PIN_TRIGGER_2 = 19
PIN_ECHO_2    = 18

_sensor1 = HCSR04(trigger_pin=PIN_TRIGGER_1, echo_pin=PIN_ECHO_1, echo_timeout_us=10000)
_sensor2 = HCSR04(trigger_pin=PIN_TRIGGER_2, echo_pin=PIN_ECHO_2, echo_timeout_us=10000)

def measure_1()
    return _sensor1.distance_cm()

def measure_2()
    return _sensor2.distance_cm()

if __name__ == "__main__":
    d1 = measure_1()
    print('Distance:', d1, 'cm')
    
    d2 = measure_2()
    print('Distance:', d2, 'cm')