from machine import Pin, SPI, Timer
import MatrixDisplay_v4 as matrix
import dotMatrix
import utime

BLINKS_PER_SECOND = 1 
timer = Timer()
#convert 1543 to tuple
def getTimeList(hours, minutes):
    return (hours // 10, hours % 10, ":"minutes // 10
            , minutes % 10)
    
def showTime( timer ):
    dt = utime.localtime()
    timeList = getTimeList(dt[3], dt[4])
    print(timeList)
    currentTime = "{}{}{}{}".format(timeList[0],timeList[1]
                                    ,timeList[2],timeList[3])
    matrix.display.fill( matrix.CLEAR_SCREEN )
    matrix.display.text( currentTime, 0, 0, matrix.PIXEL_ON)
    matrix.display.show()

timer.init(freq=BLINKS_PER_SECOND, mode=Timer.PERIODIC, callback=showTime)



