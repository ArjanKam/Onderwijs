from machine import Pin
import dht

PIN_DHT11_DATA = 0
INTERVAL_MEASUREMENT = 2  # seconds

_pinData = Pin(PIN_DHT11_DATA, Pin.IN)
_sensor = dht.DHT11(_pinData)


# convert temperature from Celsius to Fahrenheit
def toFahrenheit(celsius):
    return celsius * (9 / 5) + 32.0


def measure():
    try:
        _sensor.measure()
        return _sensor.temperature(), _sensor.humidity()
    except OSError as e:
        return 0, 0


if "__main__" == __name__:
    from time import sleep

    print('-------- 0 -------')
    measurement = 1
    while True:
        sleep(INTERVAL_MEASUREMENT)
        temp, hum = measure()
        print('-------- %d -------' % measurement)
        print('Temperature: %3.1f C' % temp)
        print('Temperature: %3.1f F' % toFahrenheit(temp))
        print('Humidity: %3.1f %%' % hum)
        measurement = measurement + 1
