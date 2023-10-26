from machine import Pin, SPI
import max7219

USE_PICO = False
NUMBER_OF_MODULES : int = 4
PSI_CHANNEL = 0

PIN_SCK = 14	# D5 (14)
PIN_MOSI = 13	# D7 (13)
PIN_CS = 15		# D8 (15)
    
LED_BRIGHTNESS = 4

CLEAR_SCREEN = 0
PIXEL_ON = 1
PIXEL_OFF = 0

_spi = SPI(1, baudrate=10000000, polarity=0, phase=0) 
_cs = Pin(PIN_CS, Pin.OUT)

display = max7219.Matrix8x8(_spi, _cs, NUMBER_OF_MODULES)
display.brightness( LED_BRIGHTNESS )

START_X = 0
START_Y = 0

def showText(tekst):
    display.fill( CLEAR_SCREEN )
    display.text( tekst, START_X, START_Y, PIXEL_ON)
    display.show()
        
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
