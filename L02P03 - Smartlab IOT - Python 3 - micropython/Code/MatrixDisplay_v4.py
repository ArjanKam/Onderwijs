from machine import Pin, SPI
import max7219

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
    
if "__main__" == __name__:
    from time import sleep
    SLEEP = 2 # second
    START_X = 0
    START_Y = 0
    
    def showText(tekst):
        display.fill( CLEAR_SCREEN )
        display.text( tekst,START_X,START_Y,PIXEL_ON)
        display.show()
        sleep( SLEEP )
    
    TEXT_1 = ' MAX'
    TEXT_2 = '7219'
    TEXT_3 = 'Test'
    while True:
        showText( TEXT_1 )
        showText( TEXT_2 )
        showText( TEXT_3 )
