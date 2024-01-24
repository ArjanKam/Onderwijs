'''[s =signal] [_ =3v3] [- =ground]'''

from machine import Pin
from time import sleep
import dht
import TC74ThermalSensor


sensor = dht.DHT11(Pin(22))

while True:
  try:
    sleep(1)
    
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print('Temperature: %3.1f C' %temp)
    print('Humidity: %3.1f %%' %hum)
    
    temp1 = TC74ThermalSensor.ReadTemperature()
    print('Temperature1: %3.1f C' %temp1,'\n')
  except OSError as e:
    print('Failed to read sensor.')





# from machine import Pin
# from time import sleep
# from dht import DHT11
# 
# dhtPin = Pin(16, Pin.IN, Pin.PULL_DOWN)
# 
# while True:
#     sleep(2)
#     dhtSensor = DHT11(dhtPin)
#     
#     temp_value = dhtSensor.temperature
#     hum_value = dhtSensor.humidity
#     
#     print("temperature : ", temp_value, " °C")
#     print("humidity : ", hum_value, " %", "\n")