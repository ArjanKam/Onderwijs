from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
from time import sleep 				# ADDED
NUMBER_OF_ROWS = 2
NUMBER_OF_COLUMNS = 16

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = <Vul hier het adres in> #i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, NUMBER_OF_ROWS, NUMBER_OF_COLUMNS)

lcd.clear()
lcd.blink_cursor_on()
lcd.putstr("daVinci")
lcd.putstr("I2C Address:"+str(I2C_ADDR)+"\n")

lcd.blink_cursor_off() 			# ADDED
lcd.clear() 						# ADDED
lcd.putstr("Backlight Test") 	# ADDED
for i in range(10): 				# ADDED
    lcd.backlight_on() 			# ADDED
    sleep(0.2) 					# ADDED
    lcd.backlight_off() 			# ADDED
    sleep(0.2) 					# ADDED
lcd.backlight_on() 				# ADDED
lcd.hide_cursor() 				# ADDED

