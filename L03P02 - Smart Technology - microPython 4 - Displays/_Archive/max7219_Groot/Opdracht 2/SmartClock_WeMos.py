from machine import Pin, SPI, Timer
import wifi
import utime, ntptime
import MatrixDisplay_WeMos as matrixDisplay
import matrixBuffer
import dotMatrix
import DHT11_v2 as DHT11

import secrets # store your SSIS and PASSWORD here
import network
BLINKS_PER_SECOND = 1 
MAX_DOTS = 4

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
    matrixDisplay.display.pixel(position, 7, 1)
    
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
    matrixDisplay.display.fill( matrixDisplay.CLEAR_SCREEN )
    matrixBuffer.setByteArray(matrixDisplay.display.framebuf, cl)
    showSeconds(seconds)
    matrixDisplay.display.show()
    
def measureTempHumidity():
    return DHT11.measure()

def initClock():
    sta_if = wifi.network.WLAN(wifi.network.STA_IF)
    sta_if.disconnect()
    wifi.connect(sta_if, matrixDisplay.showText)
    return RTC()

temp = None
humidity = None
def showOnDisplay( timer ):
    global temp, humidity
    dt = utime.localtime()
    hours   = (dt[3] + 2)%24 # +GMT + Daylight
    minutes = dt[4]
    seconds = dt[5]

    if seconds == 0 or temp == None:
        temp, humidity = measureTempHumidity()
        
    if seconds < 3:
        showTemp(temp, seconds)
    elif seconds < 6:
        showHumidity(humidity, seconds)
    else:
        showTime(hours, minutes, seconds)

#infoOutput = function(text)
def connect(infoOutput = None):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(secrets.SSID, secrets.PASSWORD)
        tries = 0
        while not sta_if.isconnected():
            if infoOutput != None:
                infoOutput("." * (tries % (MAX_DOTS + 1)))
                tries = tries + 1
            utime.sleep(1)
            pass


matrixDisplay.showText("Wifi")
connect(matrixDisplay.showText)
matrixDisplay.showText("Time")
utime.sleep(1)
ntptime.settime()
matrixDisplay.showText("Done")

timer = Timer(0)
timer.init(freq=BLINKS_PER_SECOND, mode=Timer.PERIODIC, callback=showOnDisplay)



