from machine import Pin, SPI, Timer
import max7219
import utime

BLINKS_PER_SECOND = 1

NUMBER_OF_MODULES : int = 4
PSI_CHANNEL = 0
PIN_SCK = 2
PIN_MOSI = 3
PIN_CS = 5
LED_BRIGHTNESS = 10

CLEAR_SCREEN = 0
PIXEL_ON = 1
PIXEL_OFF = 0

_spi = SPI(PSI_CHANNEL,sck=Pin( PIN_SCK ),mosi=Pin(PIN_MOSI))
_cs = Pin(PIN_CS, Pin.OUT)

display = max7219.Matrix8x8(_spi, _cs, NUMBER_OF_MODULES)
display.brightness( LED_BRIGHTNESS )
    
def showTime( timer ):
    dt = utime.localtime()
    display.fill( CLEAR_SCREEN )
    currentTime = "{}{}".format(dt[4],dt[5])
    display.text( currentTime, 0, 0, PIXEL_ON)
    display.show()
        
timer.init(freq=BLINKS_PER_SECOND, mode=Timer.PERIODIC, callback=showTime)
    
    
