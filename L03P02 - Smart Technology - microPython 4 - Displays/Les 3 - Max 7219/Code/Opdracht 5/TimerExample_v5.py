from machine import Pin, SPI, Timer
import MatrixDisplay_v4 as matrix
import matrixBuffer
import dotMatrix
import utime

BLINKS_PER_SECOND = 1 
timer = Timer()
#convert 1543 to tuple
def getTimeList(hours, minutes, seconds):
    if seconds % 2 == 0:
        seperator = "|"
    else:
        seperator = ";"
    return (hours // 10, hours % 10, seperator
            , minutes // 10, minutes % 10)
#list of elements to convert to matrix
def elementsToMatrix(ls):
    matrix = []
    for element in ls:
        matrix.append(dotMatrix.MATRIX6x8[element])
    return matrix 

def showSeconds(seconds):
    position = 1 + (seconds % 60 // 2)
    matrix.display.pixel(position, 7, 1)
    
def showTime( timer ):
    dt = utime.localtime()
    hours   = dt[3]
    minutes = dt[4]
    seconds = dt[5]
    timeList = getTimeList(hours, minutes, seconds)
    timeMatrix = elementsToMatrix(timeList)
    
    cl = matrixBuffer.setCompleteList(timeMatrix)

    matrix.display.fill( matrix.CLEAR_SCREEN )
    matrixBuffer.setByteArray(matrix.display.framebuf, cl)
    showSeconds(seconds)
    matrix.display.show()

timer.init(freq=BLINKS_PER_SECOND, mode=Timer.PERIODIC, callback=showTime)



