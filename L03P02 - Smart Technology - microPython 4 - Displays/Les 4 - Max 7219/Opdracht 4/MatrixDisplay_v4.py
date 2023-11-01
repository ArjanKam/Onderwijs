from machine import Pin, SPI
import utime
import internetData
import matrixBuffer
import max7219

NUMBER_OF_MODULES : int = 8
PIXELS_PER_MODULE : int = 8
STARTPOSITION_SECONDS = 2
DEVIDER_SECONDS = 60 // (NUMBER_OF_MODULES * 8 - (2 * STARTPOSITION_SECONDS))
PSI_CHANNEL = 0
MAX7219_SCROLL_DELAY = 50     # MAX7219 display scrolling speed (ms)

# MAX7219 driver: https://github.com/mcauser/micropython-max7219
# Note: this driver is designed for 4-in-1 MAX7219 modules.
# VCC: 3.3V or 5V
# GND: GND
# DIN: MOSI 3
# CS:  5
# CLK: SCK 2
PIN_SCK = 2
PIN_MOSI = 3
PIN_CS = 5
  
LED_BRIGHTNESS = 4

CLEAR_SCREEN = 0
PIXEL_ON = 1
PIXEL_OFF = 0

_spi = SPI(PSI_CHANNEL,sck=Pin( PIN_SCK ),mosi=Pin(PIN_MOSI))
_cs = Pin(PIN_CS, Pin.OUT)

def showText(tekst = "", x=0, y=0):
    display.fill( CLEAR_SCREEN )
    display.text( tekst, x, y, PIXEL_ON)
    display.show()
    
# display data
def data_display(timer):
    print('data_display', internetData.data_available)
    if not internetData.data_available:
        return

    # scroll text
    text = internetData.data
    textLengthPixels = len(text) * PIXELS_PER_MODULE - 1
    displayWidthPixels = NUMBER_OF_MODULES * PIXELS_PER_MODULE
    #print(textLengthPixels, displayWidthPixels, text)
    x = 0
    while x <= textLengthPixels + (2 * displayWidthPixels):
        showText(text, displayWidthPixels-x)
        utime.sleep_ms(MAX7219_SCROLL_DELAY)
        x = x + 1
        
def showSeconds(seconds):
    position = 1 + (seconds % 60 // DEVIDER_SECONDS)
    display.pixel(position, 7, STARTPOSITION_SECONDS)

def showTimeTemp(temp, hours, minutes, seconds):
    lst = matrixBuffer.getTempList(temp)
    lst+= matrixBuffer.getTimeList(hours, minutes, seconds)
    showList(lst, seconds)
    
def showTimeHum(humidity, hours, minutes, seconds):
    lst = matrixBuffer.getHumidityList(humidity)
    lst+= matrixBuffer.getTimeList(hours, minutes, seconds)
    showList(lst, seconds)

def showTime(hours, minutes, seconds):
    lst = matrixBuffer.getTimeList(hours, minutes, seconds)
    showList(lst, seconds)
    
def showTemp(temp, seconds):
    lst = matrixBuffer.getTempList(temp)
    showList(lst, seconds)

def showHumidity(humidity, seconds):
    lst = matrixBuffer.getHumidityList(humidity)
    showList(lst, seconds)
    
def showList(lst, seconds):
    timeMatrix = matrixBuffer.elementsToMatrix(lst)
    cl = matrixBuffer.setCompleteList(timeMatrix)
    display.fill( CLEAR_SCREEN )
    matrixBuffer.setByteArray(display.framebuf, cl)
    showSeconds(seconds)
    display.show()
 
 
display = max7219.Matrix8x8(_spi, _cs, NUMBER_OF_MODULES)
display.brightness( LED_BRIGHTNESS )

# display for first time...
print("Display data for first time...")
#data_display(None)
print("Service started.")

if "__main__" == __name__:
    from time import sleep
    SLEEP = 1 # second
    TEXT_1 = 'PICO'
    TEXT_2 = '1234'
    TEXT_3 = 'done'
    
    showText( TEXT_1 )
    sleep( SLEEP )
    showText( TEXT_2 )
    sleep( SLEEP )
    showText( TEXT_3 )
    sleep( SLEEP )
