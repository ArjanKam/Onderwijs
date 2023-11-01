from machine import Pin, SPI, Timer
import wifi
import utime, ntptime
import MatrixDisplay_v4 as matrixDisplay
import matrixBuffer
import dotMatrix
import DHT11_v2 as DHT11

import secrets # store your SSIS and PASSWORD here
import network
BLINKS_PER_SECOND = 1 
MAX_DOTS = 4

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

def main():
    matrixDisplay.showText("Wifi")
    connect(matrixDisplay.showText)
    matrixDisplay.showText("Time")
    utime.sleep(1)
    ntptime.settime()
    matrixDisplay.showText("Done")

    if USE_PICO == True:
        timer = Timer()
    else: #WeMos
        timer = Timer(0)
    timer.init(freq=BLINKS_PER_SECOND, mode=Timer.PERIODIC, callback=showOnDisplay)

main()

