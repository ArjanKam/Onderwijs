from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
from time import sleep 				# ADDED
NUMBER_OF_ROWS = 2
NUMBER_OF_COLUMNS = 16

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = <Vul hier het adres in> #i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, NUMBER_OF_ROWS, NUMBER_OF_COLUMNS)

SMILE = ( 0b00000,
          0b00000,
          0b01010,
          0b00000,
          0b10001,
          0b10001,
          0b01110,
          0b00000)

lcd.clear()
lcd.hide_cursor()
lcd.custom_char(0,SMILE)
lcd.move_to(8,1)
lcd.putchar(chr(0))



