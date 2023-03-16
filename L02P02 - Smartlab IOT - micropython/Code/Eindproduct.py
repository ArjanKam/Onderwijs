from machine import Pin, SoftI2C
import ssd1306
from time import sleep
from machine import Pin
import time
import ULTRASONE_HC_SR04 as hcsr04

SLEEP       = 1000 # 1 seconden
PIN_D = (16, 5, 4, 0, 2, 14, 12, 13, 15)
OLED_WIDTH = 128
OLED_HEIGHT = 64
TEXT_BTTM_LOCATION = 55
TEXT_HEIGHT = OLED_HEIGHT - TEXT_BTTM_LOCATION
OLED_GRAPH_TOP  = 0
OLED_GRAPH_BTTM = TEXT_BTTM_LOCATION - 1
BAK_LEEG = 20 # cm
BAK_VOL = 5 #cm

ultrasonic = hcsr04.HCSR04(trigger_pin=PIN_D[7], echo_pin=PIN_D[6],
                           echo_timeout_us=1000000)
i2c = SoftI2C(scl=Pin(PIN_D[1]), sda=Pin(PIN_D[2]))
oled = ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)
oled.text('Lenspomp 21-22', 5, TEXT_BTTM_LOCATION)
oled.rect(0, 0, OLED_WIDTH, TEXT_BTTM_LOCATION-5, 1)
oled.rect(5, 0, OLED_WIDTH-10, TEXT_BTTM_LOCATION-10, 0)
oled.show()
sleep(2) # toon text 5 seconden op scherm

while True:
    time.sleep_ms(SLEEP)
    distance = ultrasonic.distance_cm()
    print('Distance:', distance, 'cm', '|')
    
    oled.rect(0, TEXT_BTTM_LOCATION, OLED_WIDTH, TEXT_HEIGHT, 0) #clear text
    tekst = "Hoogte {:.2f} cm".format(distance)
    oled.text(tekst, 0, TEXT_BTTM_LOCATION)
    
    # reset waterhoogte
    oled.rect(5, 0, OLED_WIDTH-10, TEXT_BTTM_LOCATION-10, 0)
    if distance < BAK_LEEG:
        h = int((distance - 5 ) /(BAK_LEEG - BAK_VOL)* TEXT_BTTM_LOCATION)
        oled.rect(8, h, OLED_WIDTH-16, TEXT_BTTM_LOCATION-13-h, 1)

    oled.show()