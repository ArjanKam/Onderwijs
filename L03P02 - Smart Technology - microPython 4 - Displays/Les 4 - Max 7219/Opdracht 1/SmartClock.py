from machine import Pin, SPI, Timer, RTC
import MatrixDisplay_v4 as matrix
import matrixBuffer
import dotMatrix
import utime
from time import sleep
import DHT11_v2 as DHT11
import wifi

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

def getTempList(temp):
    tempList = []
    negative = temp < 0
    if negative:
        tempList.append("-")
        temp = temp * -1
    
    if temp >= 100:
        honderds = temp // 100
        temp = temp - (honderds * 100)
        tempList.append(honderds // 10)
        tempList.append(temp // 10)
        tempList.append(temp % 10)
    else:
        if not negative:
            tempList.append(" ")
        if temp > 10:
            tempList.append(temp // 10)
            tempList.append(temp % 10)
        else:
             tempList.append(" ")
             tempList.append(temp % 10)
          
    tempList.append("|")
    tempList.append("C")
    return tuple(tempList)

def getHumidityList(humidity):
    if humidity >= 100:
        return (1, 0, 0, "%")
    return (" ", humidity // 10, humidity % 10, "%")

#list of elements to convert to matrix
def elementsToMatrix(ls):
    matrix = []
    for element in ls:
        matrix.append(dotMatrix.MATRIX6x8[element])
    return matrix 

def showSeconds(seconds):
    position = 1 + (seconds % 60 // 2)
    matrix.display.pixel(position, 7, 1)
    
def showTime(hours, minutes, seconds):
    lst = getTimeList(hours, minutes, seconds)
    showList(lst, seconds)
    
def showTemp(temp, seconds):
    lst = getTempList(temp)
    showList(lst, seconds)

def showHumidity(humidity, seconds):
    lst = getHumidityList(humidity)
    showList(lst, seconds)
    
def showList(lst, seconds):
    timeMatrix = elementsToMatrix(lst)
    cl = matrixBuffer.setCompleteList(timeMatrix)
    matrix.display.fill( matrix.CLEAR_SCREEN )
    matrixBuffer.setByteArray(matrix.display.framebuf, cl)
    showSeconds(seconds)
    matrix.display.show()
    
def measureTempHumidity():
    return DHT11.measure()


def initClock():
    matrix.display.fill( matrix.CLEAR_SCREEN )
    wifi.connect(wifi.network.WLAN(wifi.network.STA_IF), matrix.showText)    
    return RTC().datetime()

temp = None
humidity = None
lastDay = None
def showOnDisplay( timer ):
    global temp, humidity, lastDay
    dt = RTC().datetime()
    hours   = dt[4] # + 2 ) % 24 #bug with timezone
    minutes = dt[5]
    seconds = dt[6]
    
    if dt[2] != lastDay:
        dt = initClock()
        hours   = dt[4] # + 2 ) % 24 #bug with timezone
        minutes = dt[5]
        seconds = dt[6]
        lastDay = dt[2]

    if seconds == 0 or temp == None:
        temp, humidity = measureTempHumidity()
        
    if seconds < 3:
        showTemp(temp, seconds)
    elif seconds < 6:
        showHumidity(humidity, seconds)
    else:
        showTime(hours, minutes, seconds)

matrix.showText("1")
sleep(1)
dt = initClock()
matrix.showText("2")
sleep(1)
timer.init(freq=BLINKS_PER_SECOND, mode=Timer.PERIODIC, callback=showOnDisplay)



