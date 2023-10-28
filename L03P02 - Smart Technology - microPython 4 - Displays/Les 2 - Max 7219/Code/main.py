import pixelEatPixel as pep
import MatrixDisplay_v4 as matrix
import WaterLevelApp as wl

while True:
    wl.run()
    
    matrix.showText("SMART TECHNOLOGY ELEKTRO", 0,0, True)
    
    pep.showRect()
    pep.run()
