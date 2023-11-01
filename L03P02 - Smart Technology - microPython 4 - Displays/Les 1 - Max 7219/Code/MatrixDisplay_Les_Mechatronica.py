from machine import Pin, SPI
import max7219
from time import sleep

spi = SPI(0,sck=Pin(2),mosi=Pin(3))
cs = Pin(5, Pin.OUT)

display = max7219.Matrix8x8(spi, cs, 4)
display.brightness(10)

def toonText(tekst, x, y):
    display.fill(0)
    display.text(tekst,x,y,1)
    display.show()

tekst = "Hallo"
x = -7
while True:
    toonText(tekst, x, x)
    sleep(0.3)
    x = x + 1
    if x > 7:
        x = -7
        tekst = "dag"
    

   