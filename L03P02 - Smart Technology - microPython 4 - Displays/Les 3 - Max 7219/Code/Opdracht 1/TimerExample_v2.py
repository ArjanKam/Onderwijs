from machine import Pin, SPI, Timer
import MatrixDisplay_v4 as matrix
import utime

BLINKS_PER_SECOND = 2 
timer = Timer()

def blink( timer ):
    dt = utime.localtime()
    strTime = "{:02d}{:02d}".format(dt[3], dt[4])
    matrix.display.fill( matrix.CLEAR_SCREEN )
    matrix.display.text( strTime, posX, posY, matrix.PIXEL_ON)
    matrix.display.show()
    
timer.init(freq=BLINKS_PER_SECOND, mode=Timer.PERIODIC, callback=blink)



