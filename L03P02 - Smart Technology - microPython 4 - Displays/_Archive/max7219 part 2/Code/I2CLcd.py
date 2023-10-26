#https://www.tomshardware.com/how-to/lcd-display-raspberry-pi-pico
from machine import I2C, Pin
from utime import sleep
from pico_i2c_lcd import I2cLcd
HEIGHT = 2
WIDTH = 16

_i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = _i2c.scan()[0]
_lcd = I2cLcd(_i2c, I2C_ADDR, HEIGHT, WIDTH)

def clear():
    _lcd.clear()
    
def write(text, x=0, y=0):
    _lcd.move_to(x,y)
    _lcd.putstr(text)
    
def writeLine(text, lineNumer = 0):
    _lcd.move_to(0, lineNumer)
    _lcd.putstr(text)
    
if __name__ == "__main__":
    while True:
        print(I2C_ADDR)
        _lcd.blink_cursor_on()
        _lcd.putstr("I2C Address:"+str(I2C_ADDR)+"\n")
        _lcd.putstr("Tom's Hardware")
        
        sleep(2)
        _lcd.clear()
        _lcd.putstr("I2C Address:"+str(hex(I2C_ADDR))+"\n")
        _lcd.putstr("Tom's Hardware")
        
        sleep(2)
        _lcd.blink_cursor_off()
        _lcd.clear()
        _lcd.putstr("Backlight Test")
        for i in range(10):
            _lcd.backlight_on()
            sleep(0.2)
            _lcd.backlight_off()
            sleep(0.2)
        _lcd.backlight_on()
        _lcd.hide_cursor()
        
        for i in range(20):
            _lcd.putstr(str(i))
            sleep(0.4)
            _lcd.clear()
