from machine import Pin
import neopixel
import neoPixelHelper as helper

PIN_DIN = 28
_np = neopixel.NeoPixel(Pin(PIN_DIN), helper.TOTAL_PIXELS)

def clear():
    for index in helper.getAllPixels():
        _np[index] = COLOR_BLACK
    _np.write()

#firstStrip is boolean
#index is the index of that strip
def showPixel(firstStrip, index, color):
    index = helper.getPixel(firstStrip, index)
    _np[index] = color
    _np.write()
    
#pixels is a list of tuples (index, color)
def showPixels(pixels):
    for pixel in pixels:
        _np[pixel[0]] = pixel[1]
    _np.write()
       
clear()

if __name__ == "__main__":
          
    color = 1
    direction = 10
    while True:
        x = random.choice(strip1)
        r= random.randint(0, 255)
        g= random.randint(0, 255)
        b= random.randint(0, 255)
        showPixel(True, x, (r,g,b))
        showPixel(True, x, COLOR_BLACK)

