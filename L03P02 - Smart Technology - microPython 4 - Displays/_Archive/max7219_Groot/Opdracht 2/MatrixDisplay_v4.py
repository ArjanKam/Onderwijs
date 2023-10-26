from machine import Pin, SPI
import max7219

NUMBER_OF_MODULES : int = 4
PSI_CHANNEL = 0

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
    
display = max7219.Matrix8x8(_spi, _cs, NUMBER_OF_MODULES)
display.brightness( LED_BRIGHTNESS )
showText()

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
