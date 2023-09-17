from machine import Pin, SoftI2C
import ssd1306
from time import sleep
import pressureMeasurement as pressure
PIN_D = (16, 5, 4, 0, 2, 14, 12, 13, 15)
OLED_WIDTH = 128
OLED_HEIGHT = 64
TEXT_BTTM_LOCATION = 57
OLED_GRAPH_TOP  = 0
OLED_GRAPH_BTTM = TEXT_BTTM_LOCATION - 1

i2c = SoftI2C(scl=Pin(PIN_D[1]), sda=Pin(PIN_D[2]))
oled = ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)
oled.text('LensPomp 2022', 10, TEXT_BTTM_LOCATION)
oled.show()

pixels = []
x = 0
while True:
    sleep(0.005)
    y = pressure.getMeasurement(OLED_WIDTH, OLED_GRAPH_BTTM)
    if len(pixels) <= x:
        pixels.append(y)
    else:
        oled.pixel(x, pixels[x], 0)
    oled.pixel(x, y, 1)
    pixels[x] = y
    x += 1
    if x > OLED_WIDTH:
        x = 0
    oled.show()