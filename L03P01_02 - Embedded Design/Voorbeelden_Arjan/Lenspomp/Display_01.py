from machine import Pin, SoftI2C
import ssd1306
from time import sleep
import math
PIN_D = (16, 5, 4, 0, 2, 14, 12, 13, 15)
OLED_WIDTH = 128
OLED_HEIGHT = 64
TEXT_BTTM_LOCATION = 57
OLED_GRAPH_TOP  = 0
OLED_GRAPH_BTTM = TEXT_BTTM_LOCATION - 1
OLED_HALF_HEIGHT = OLED_GRAPH_BTTM // 2
i2c = SoftI2C(scl=Pin(PIN_D[1]), sda=Pin(PIN_D[2]))
oled = ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)
oled.text('LensPomp 2022', 10, TEXT_BTTM_LOCATION)
oled.show()
def measurement(x):
    rad = (3* x / (OLED_WIDTH)) * math.pi
    y = OLED_HALF_HEIGHT * (1 + math.sin(rad))
    return int(y)
pixels = []
x = 0
teller = 0
while True:
    sleep(0.005)
    y = measurement(teller)
    teller += 1
    if len(pixels) <= x:
        pixels.append(y)
    else:
        oled.pixel(x, pixels[x], 0)
    oled.pixel(x, y, 1)
    pixels[x] = y
    print(pixels[x])
    x += 1
    if x > OLED_WIDTH:
        x = 0
    oled.show()