from machine import Pin, SPI
import max7219
from utime import sleep

NUMBER_OF_MODULES : int = 12
PSI_CHANNEL = 0
PIN_SCK = 2
PIN_MOSI = 3
PIN_CS = 5
LED_BRIGHTNESS = 1
SLEEP = 2 # second

CLEAR_SCREEN = 0
PIXEL_ON = 1
PIXEL_OFF = 0

_spi = SPI(PSI_CHANNEL,sck=Pin( PIN_SCK ),mosi=Pin(PIN_MOSI))
_cs = Pin(PIN_CS, Pin.OUT)

display = max7219.Matrix8x8(_spi, _cs, NUMBER_OF_MODULES)
display.brightness( LED_BRIGHTNESS )

def clear( on ):
    display.fill( on )
    display.show()
    
def showText(tekst, x = 0, y = 0, centered = False, show = True, clear = True):
    length = len(tekst)
    if clear:
        display.fill( CLEAR_SCREEN )
    
    if length > NUMBER_OF_MODULES:
        x = NUMBER_OF_MODULES * 8
        while x > -length * 8:
            display.text( tekst,x,y,PIXEL_ON)
            display.show()
            display.text( tekst,x,y,PIXEL_OFF)
            x -= 1
            sleep( 0.1 )
    else:
        if centered:
            dx = len(tekst) // 2
            x = (NUMBER_OF_MODULES // 2 - dx) * 8
        display.text( tekst,x,y,PIXEL_ON)
        if show:
            display.show()
            
#y is offset in y direction. the char will be filled
#with the 
def showCharacter(char, x = 0, y = 0, reversePixel = False):
    height = len(char)
    dy = 0
    for row in char:
        dx = 0
        for pixel in row:
            display.pixel(x + dx, y + dy, pixel != reversePixel)
            dx += 1
        dy += 1
        if y + dy >= height:
            return

if "__main__" == __name__:
    from utime import sleep
    md.clear(0)
    if True:
        y = 0
        while True:
            showCharacter(ARROW_D,  0, -32 + y)
            showCharacter(ARROW_U, 16, -y)
            md.display.show()
            sleep(0.1)
            y += 1
            if y == 32:
                y = 0
                
    TEXT_1 = ' MAX'
    TEXT_2 = '7219'
    TEXT_3 = 'Test'
    while True:
        showText( TEXT_1 )
        showText( TEXT_2 )
        showText( TEXT_3 )


