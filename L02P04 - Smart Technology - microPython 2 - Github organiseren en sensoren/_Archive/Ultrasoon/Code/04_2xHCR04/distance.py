from hcsr04 import HCSR04

# (TRIGGER, ECHO)
PIN ( (21,20), (19,18) )

_sensors = []
for pin in PIN:
    _sensors.append( HCSR04(trigger_pin=pin[0], echo_pin=pin[1], echo_timeout_us=10000) )

def measure_all():
    distances = []
    for sensor in _sensors:
        distances.append(sensor.distance_cm())
    return distances

def measure(index):
    return _sensors[index].distance_cm()

if __name__ == "__main__":
    d = measure_all()
    print('Distances:', d, 'cm')
    
    for index in range(len(_sensors)):
        d2 = measure(index)
        print('Distance:', d2, 'cm')
