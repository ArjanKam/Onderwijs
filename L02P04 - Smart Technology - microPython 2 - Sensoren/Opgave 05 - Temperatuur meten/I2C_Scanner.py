from machine import I2C, Pin

i2c = I2C(id = 0, sda=Pin(0), scl=Pin(1))
devices = i2c.scan()

print('Scan i2c bus...')
if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))

  for device in devices:  
    print("Decimal address: ",device," | Hexa address: ",hex(device))


