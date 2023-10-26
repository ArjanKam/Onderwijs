import MatrixDisplay_v4 as md
from utime import sleep
import random

WIDTH  = md.NUMBER_OF_MODULES * 8
HEIGHT = 8
OFFSET_X = 15 # offset x-start pos of pixel

MOVES_SLEEP = 0.1
SCORE_SLEEP = 2

def getNexPos(pos):
    dx = random.randint(-1,1)
    dy = random.randint(-1,1)
    pos[0] += dx
    pos[1] += dy
    if pos[1] < 0:
        pos[1] = 0
    if pos[0] < 0:
        pos[0] = 0
    if pos[1] > HEIGHT - 1:
        pos[1] = HEIGHT - 1 
    if pos[0] > WIDTH - 1:
        pos[0] = WIDTH - 1 
    return pos

def showRect():
    x = 0
    y = 0
    while x < 4:
        md.display.rect(x,x, WIDTH-x-x, HEIGHT-x-x, 1)
        md.display.show()
        sleep(MOVES_SLEEP)
        md.display.rect(x,x, WIDTH-x-x, HEIGHT-x-x, 0)
        x += 1
    
def showPixel(pos):
    md.display.pixel(pos[0],pos[1],1)
    md.display.show()
    #sleep(MOVES_SLEEP)
    md.display.pixel(pos[0],pos[1],0)
    md.display.show()
    #sleep(MOVES_SLEEP)
        
def run():   
    md.clear( True )
    pos1 = [        OFFSET_X, HEIGHT//2]
    pos2 = [WIDTH - OFFSET_X, HEIGHT//2]
    moves = 0
    while pos1 != pos2:
        showPixel(pos1)
        showPixel(pos2)
        pos1 = getNexPos(pos1)
        pos2 = getNexPos(pos2)
        moves += 1
        
    md.showText(str(moves), 0,0, True)
    sleep(SCORE_SLEEP)
    
    showRect()




