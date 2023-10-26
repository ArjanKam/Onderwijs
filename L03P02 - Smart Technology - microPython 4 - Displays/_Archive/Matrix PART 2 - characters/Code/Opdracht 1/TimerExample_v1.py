from machine import Timer
import utime
import dotMatrix as mc

BLINKS_PER_SECOND = 1 
timer = Timer()  # or Timer(0)

def combineMatrix(listOfChars):
    allCharacters = []
    y = 0
    while y < len(listOfChars[0]):
        line = []
        for c in listOfChars:
            line = line + list(c[y])
        allCharacters.append(list(line))
        y = y + 1            
    return allCharacters6

def blink( paramTimer ):
    dt = utime.localtime()
    strTime = "{:02d}:{:02d}".format(dt[3], dt[4])
    matrixList = []
    for x in list(strTime):
        matrixList.append(mc.MATRIX6x8[x])
    matrix = combineMatrix(matrixList)
    mc.printMatrix(matrix)
    print("----")
timer.init(freq=BLINKS_PER_SECOND, mode=Timer.PERIODIC, callback=blink)

