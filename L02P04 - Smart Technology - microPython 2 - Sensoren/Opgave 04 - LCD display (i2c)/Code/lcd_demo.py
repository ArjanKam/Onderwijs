from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

I2C_ADDR = <> #i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

ARROW_0 = (0b00100,0b01110,0b10101,0b00100,0b00100,0b00100,0b00100,0b00100)
ARROW_1 = (0b01110,0b10101,0b00100,0b00100,0b00100,0b00100,0b00100,0b00100)
ARROW_2 = (0b10101,0b00100,0b00100,0b00100,0b00100,0b00100,0b00100,0b01110)
ARROW_3 = (0b00100,0b00100,0b00100,0b00100,0b00100,0b00100,0b01110,0b10101)
ARROW_4 = (0b00100,0b00100,0b00100,0b00100,0b01110,0b10101,0b00100,0b00100)
ARROW_5 = (0b00100,0b00100,0b00100,0b01110,0b10101,0b00100,0b00100,0b00100)
ARROW_6 = (0b00100,0b00100,0b01110,0b10101,0b00100,0b00100,0b00100,0b00100)
ARROWS  = (ARROW_0,ARROW_1,ARROW_2,ARROW_3,ARROW_4,ARROW_5, ARROW_6)
ARROW   = (0b00100,0b01110,0b10101,0b00100,0b00100,0b00100,0b00100,0b00100)

for index, arrow in enumerate(ARROWS):
    lcd.custom_char(index,arrow)

while True:
    if False:
        lcd.clear()
        for i in range(3):
            for x in range(len(ARROWS)):
                lcd.move_to(0,0)
                lcd.putchar(chr(x))
                sleep(1)
    if False:
        lcd.clear()
        print(I2C_ADDR)
        lcd.blink_cursor_on()
        lcd.putstr("I2C Address:"+str(I2C_ADDR)+"\n")
        lcd.putstr("Tom's Hardware")
        sleep(2)
    if False:
        lcd.clear()
        lcd.putstr("I2C Address:"+str(hex(I2C_ADDR))+"\n")
        lcd.putstr("Tom's Hardware")
        sleep(2)
    if False:
        lcd.blink_cursor_off()
        lcd.clear()
        lcd.putstr("Backlight Test")
        for i in range(10):
            lcd.backlight_on()
            sleep(0.2)
            lcd.backlight_off()
            sleep(0.2)
        lcd.backlight_on()
        lcd.hide_cursor()
    if True:
        lcd.clear()
        lcd.putstr("Countdown : ")
        countdown = 20
        while countdown >= 0:
            lcd.move_to(13, 0)
            lcd.putstr(str(countdown))
            sleep(0.4)
            countdown -= 1
