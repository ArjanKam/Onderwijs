from machine import Pin, SPI
import max7219
from time import sleep

NUMBER_OF_MODULES : int = 4
PSI_CHANNEL = 0
PIN_SCK = 2
PIN_MOSI = 3
PIN_CS = 5
LED_BRIGHTNESS = 10

SLEEP = 1 # second
CLEAR_SCREEN = 0
PIXEL_ON = 1
PIXEL_OFF = 0

TEXT_1 = 'PICO'
TEXT_2 = '1234'
TEXT_3 = 'done'

START_X = 0
START_Y = 0

spi = SPI(PSI_CHANNEL,sck=Pin( PIN_SCK ),mosi=Pin(PIN_MOSI))
cs = Pin(PIN_CS, Pin.OUT)

display = max7219.Matrix8x8(spi, cs, NUMBER_OF_MODULES)

display.brightness( LED_BRIGHTNESS )

def showText(tekst):
    display.fill( CLEAR_SCREEN )
    display.text( tekst,START_X,START_Y,PIXEL_ON)
    display.show()
    sleep( SLEEP )
    
while True:
    showText( TEXT_1 )
    showText( TEXT_2 )
    showText( TEXT_3 )
