from machine import Pin, SPI, Timer, reset
import utime
import MatrixDisplay_v4_WeMos as matrixDisplay
import matrixBuffer
import dotMatrix
import DHT11_v2 as DHT11
import internetData

import secrets # store your SSIS and PASSWORD here
import network
USE_PICO = False
BLINKS_PER_SECOND = 1
MESSAGE_TIME = (len(internetData.FORMAT) + matrixDisplay.NUMBER_OF_MODULES) * 8 * matrixDisplay.MAX7219_SCROLL_DELAY + 2000
DISPLAY_TIMER_DELAY  = max(MESSAGE_TIME, 5 * 60 * 1000)
     
def measureTempHumidity():
    return DHT11.measure()

temp = None
humidity = None
def clock_display( timer ):
    #print('clock_display')
    global temp, humidity
    dt = utime.localtime()
    hours   = (dt[3] + 2)%24 # +GMT + Daylight
    minutes = dt[4]
    seconds = dt[5]

    if seconds == 0 or temp == None:
        temp, humidity = measureTempHumidity()
        
    if seconds < 3:
        matrixDisplay.showTemp(temp, seconds)
    elif seconds < 6:
        matrixDisplay.showHumidity(humidity, seconds)
    else:
        matrixDisplay.showTime(hours, minutes, seconds)

# initialize timers
print("Start timers...")
timer_clock    = Timer(-1)
timer_display  = Timer(-1)

timer_clock.init(freq=BLINKS_PER_SECOND, mode=Timer.PERIODIC, callback=clock_display)
timer_display.init(period=DISPLAY_TIMER_DELAY, mode=Timer.PERIODIC, callback=matrixDisplay.data_display)

