from machine import Pin, SPI, Timer
import MatrixDisplay_v4 as matrix
import utime

BLINKS_PER_SECOND = 1 
timer = Timer()

def showTime( timer ):
    dt = utime.localtime()
    print(dt)
    currentTime = "{:02d}{:02d}".format(dt[3], dt[5])
    matrix.display.fill( matrix.CLEAR_SCREEN )
    matrix.display.text( currentTime, 0, 0, matrix.PIXEL_ON)
    matrix.display.show()

timer.init(freq=BLINKS_PER_SECOND, mode=Timer.PERIODIC, callback=showTime)



