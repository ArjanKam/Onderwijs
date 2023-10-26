from machine import Pin, SPI
import max7219 as matrix
import utime

spi = SPI(0,sck=Pin(2),mosi=Pin(3))
cs = Pin(5, Pin.OUT)

display = matrix.Matrix8x8(spi, cs, 4)
display.brightness(1)

if __name__ == "__main__":
    while True:
        dt = utime.localtime()
        print(dt)
        tijd = "{:02d}{:02d}".format(dt[3], dt[4])
    
        display.fill(0)
        display.text(tijd,0,0,1)
        display.show()
        
        if dt[5] % 10 == 0:
            x = 0
            while x < 4:
                display.rect(x,x,32-x-x,8-x-x,1)
                display.show()
                utime.sleep(.3)
                display.rect(x,x,32-x-x,8-x-x,0)
                x = x + 1
        
    
