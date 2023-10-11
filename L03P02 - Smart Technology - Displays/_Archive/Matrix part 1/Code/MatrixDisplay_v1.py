from machine import Pin, SPI
import max7219
from time import sleep
import utime

spi = SPI(0,sck=Pin(2),mosi=Pin(3))
cs = Pin(5, Pin.OUT)

display = max7219.Matrix8x8(spi, cs, 4)

display.brightness(10)

if __name__ == "__main__":
    while True:
        DEMO1 = False
        DEMO2 = True
        dt = utime.localtime()
        currentTime = "{}{}".format(dt[3],dt[4])
        display.fill(0)
        display.text(currentTime,0,0,1)
        display.show()
        print(currentTime, dt[5])
        if dt[5] %60 == 59:
            print("overgang")
            x = -1
            while x < 4:
                x1 = 0
                while x1 < x:
                    display.rect(x1, x1, 32 - x1 - x1, 8 -x1 - x1, 0)
                    x1 = x1 + 1
                display.rect(x, x, 32 - x - x, 8 -x - x, 1)
                display.show()
                
                sleep(1)
                x = x + 1
            
        if DEMO1 == True:
            display.fill(0)
            display.text('PICO',0,0,1)
            display.show()
            sleep(1)

            display.fill(0)
            display.text('1234',0,0,1)
            display.show()
            sleep(1)

            display.fill(0)
            display.text('done',0,0,1)
            display.show()
            sleep(1)
