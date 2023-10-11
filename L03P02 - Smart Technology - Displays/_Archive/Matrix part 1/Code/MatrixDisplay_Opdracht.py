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
    SLEEP_SHORT = .5 # second
    START_X = 0
    START_Y = 0
    
    def showText(tekst, x, y):
        display.fill( CLEAR_SCREEN )
        display.text( tekst, x, y,PIXEL_ON)
        display.show()
        sleep( SLEEP )
        
    TEXT_1 = 'PICO'
    # Iedere keer opnieuw tonen
    if False:
        x = START_X
        y = START_Y
        while y > - 10:
            showText( TEXT_1, x, y )
            x = x + 1
            y = y - 1
    
    #verplaatsen #1 -> gaat goed 
    if True:
        showText( TEXT_1, START_X, START_Y )
        x = 0
        while x < 10:
            display.scroll(1, -1)
            display.show()
            sleep( SLEEP )
            x = x + 1
    #verplaatsen #2 gaat niet goed-> maar geeft pixels die niet uitgaan
    if False:
        showText( TEXT_1, START_X, START_Y )
        x = 0
        while x < 10:
            display.scroll(1, 1)
            display.show()
            sleep( SLEEP )
            x = x + 1
    #teken vierkantje
    if False:
        display.fill( CLEAR_SCREEN )
        display.rect( 0,0, 32, 8,PIXEL_ON)
        display.show()
        sleep( SLEEP )
        
    while False:
        x = 0
        while x < 4 :
            display.fill( CLEAR_SCREEN )
            display.rect( x,x, 32-x-x, 8-x-x,PIXEL_ON)
            display.show()
            sleep( SLEEP_SHORT )
            x = x + 1
        display.fill( CLEAR_SCREEN )
        display.show()
        sleep( SLEEP_SHORT )