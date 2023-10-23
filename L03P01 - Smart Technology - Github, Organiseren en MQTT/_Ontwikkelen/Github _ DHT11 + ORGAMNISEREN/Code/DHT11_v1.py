from machine import Pin
from time import sleep
import dht 

PIN_DHT11_DATA = 0
INTERVAL_MEASUREMENT = 2 # seconds

pinData = Pin(PIN_DHT11_DATA, Pin.IN)
sensor = dht.DHT11(pinData)

while True:
  try:
    sleep(INTERVAL_MEASUREMENT)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    print('Temperature: %3.1f C' %temp)
    print('Temperature: %3.1f F' %temp_f)
    print('Humidity: %3.1f %%' %hum)
  except OSError as e:
    print('Failed to read sensor.')
    
