import InternalLed_v1
# import DHT11_v1
import DHT11_v2

from time import sleep

def blink():
    InternalLed_v1.on()
    sleep(.2)
    InternalLed_v1.off()
    sleep(.2)
    InternalLed_v1.on()
    sleep(.2)
    InternalLed_v1.off()


measurement = 1
while True:
    blink()

    temp, hum = DHT11_v2.measure()
    print('-------- %d -------' % measurement)
    print('Temperature: %3.1f C' % temp)
    print('Temperature: %3.1f F' % DHT11_v2.toFahrenheit(temp))
    print('Humidity: %3.1f %%' % hum)
    measurement = measurement + 1

    sleep(DHT11_v2.INTERVAL_MEASUREMENT)
