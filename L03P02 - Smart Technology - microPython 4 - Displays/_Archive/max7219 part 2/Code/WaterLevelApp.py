import character as ch
import MatrixDisplay_v4 as md
import colorHelper
import meetWaterLevelTest as measure
#import meetWaterLevelUltrasoon as measure
import neoPixelStrip as np
import I2CLcd as lcd
from utime import sleep

MOVES_SLEEP = 0.1
# NeoPixel Constants
HEIGHT_FULL  = 10
HEIGHT_EMPTY = 100
ALARM_TOP    = 20
ALARM_BOTTUM = 90
WARNING_TOP  = 40
WARNING_BOTTUM = 70

#matrix Constants
XPOS_ARROW_1 = 32
XPOS_ARROW_2 = 56
XPOS_TEXT_1 =  0
XPOS_TEXT_2 = 64

def run():
    teller = 0
    for level1, level2, level2Up in measure.getWaterLevel():
        showWaterLevel(level1, level2, level2Up)       
        sleep(MOVES_SLEEP)
        teller += 1
        if teller > 1000:
            return

def showWaterLevel(level1, level2, level2Up):
    neoPixelWaterLevel(level1, level2)
    
    showLevel(level1, level2, False)
    showArrows(level2Up, True)

    #showLevelOnLcd(level1, level2, level2Up)
    
def getNeoPixelIndex(level):
    return level * np.PIXELS_STRIP // HEIGHT_EMPTY

def colorForLevel(level):
    if level < ALARM_TOP or level > ALARM_BOTTUM:
        return colorHelper.COLOR_RED
    if level < WARNING_TOP or level > WARNING_BOTTUM:
        return colorHelper.COLOR_ORANGE
    return colorHelper.COLOR_GREEN

def neoPixelWaterLevel(level1, level2):
    np.showPixels(True,  0, getNeoPixelIndex(level1), colorForLevel(level1, HEIGHT_EMPTY))
    np.showPixels(False, 0, getNeoPixelIndex(level2), colorForLevel(level2, HEIGHT_EMPTY))

def showLevelOnLcd(level1, level2):
    lcd.clear()
    lcd.write("{:02d}cm".format(level1))
    lcd.write("{:02d}cm".format(level2), 1)
    
def showLevel(level1, level2, show = True):
    md.showText("{:2d}cm".format(level1), x=XPOS_TEXT_1, show = False, clear = True)
    md.showText("{:2d}cm".format(level2), x=XPOS_TEXT_2, show = False, clear = False)
    if show:
        md.display.show()
        
_posY = 0
def showArrows(level2Up = True, show = True):
    global _posY    
    charD = ch.getScrollingChar(ARROW_D,  _posY)
    charU = ch.getScrollingChar(ARROW_U, -_posY)
    _posY += 1
    
    if level2Up:
        xposD = XPOS_ARROW_1
        xposU = XPOS_ARROW_2
    else:
        xposD = XPOS_ARROW_2
        xposU = XPOS_ARROW_1
    md.showCharacter(charD, x=xposD)
    md.showCharacter(charU, x=xposU)    

    if show:
        md.display.show()

if __name__ == "__main__":
    run()
#     XPOS_ARROW_1 = 0
#     XPOS_ARROW_2 = 16
#     level = 0
#     while True:
#         showArrows(True, True)
#         sleep(0.05)
#        level += 1