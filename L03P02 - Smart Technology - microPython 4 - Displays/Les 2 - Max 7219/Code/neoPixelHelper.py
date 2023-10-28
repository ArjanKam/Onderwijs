import colorHelper

PIXELS_STRIP = 144
TOTAL_PIXELS = 2 * PIXELS_STRIP
MAX_PIXEL_IDEX = TOTAL_PIXELS - 1

_strip1 = []
_strip2 = []
_pixel = 0
while _pixel < PIXELS_STRIP:
    _strip1.append(_pixel)
    _strip2.append(MAX_PIXEL_IDEX - _pixel)
    _pixel += 1

def getAllPixels():
    return _strip1 + _strip2

def _getPixels(strip, startIndex, endIndex, color):
    pixels = []
    index = 0
    for x in strip:
        if index < startIndex or index > endIndex:
            pixels.append((x, colorHelper.COLOR_BLACK))
        else:
            pixels.append((x, color))
        index += 1
    return pixels

def getPixel(firstStrip, index):
    if firstStrip:
        return _strip1[index]
    return _strip2[index]

def getPixels(firstStrip, startIndex, endIndex, color):
    if firstStrip:
        return _getPixels(_strip1, startIndex, endIndex, color)
    return _getPixels(_strip2, startIndex, endIndex, color)

def _countColor(pixels, color):
    count = 0
    for p in pixels:
        if p[1] == color:
            count += 1
    return count
def _print(pixels):
    for x in pixels:
        if x[1] == colorHelper.COLOR_BLACK:
            print("_", end="")
        elif x[1] == colorHelper.COLOR_GREEN:
            print("G", end="")
        elif x[1] == colorHelper.COLOR_ORANGE:
            print("O", end="")
        elif x[1] == colorHelper.COLOR_RED:
            print("R", end="")
        else:
            print("X", end="")
    print()
            
if __name__ == "__main__":
    height = 100
    pixels1 = getPixels(True,  0, height, colorHelper.COLOR_RED)
    pixels2 = getPixels(False, 0, PIXELS_STRIP-height, colorHelper.COLOR_RED)
    
    print("Start tests")
    
    assert len(getAllPixels()) == TOTAL_PIXELS, "Should be TOTAL_PIXELS"
    assert len(pixels1) == PIXELS_STRIP, "Should be 144"
    assert _countColor(pixels1, colorHelper.COLOR_RED) == 101, "Should be 101"
    assert _countColor(pixels2, colorHelper.COLOR_RED) == 45,  "Should be 44"
    
    print("All tests OK")
    
    _print(pixels1)
    _print(pixels2)
    