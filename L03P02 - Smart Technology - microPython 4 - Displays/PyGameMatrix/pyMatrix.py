import pygame
import pygame.sysfont as sysfont
import random

COLOUR_BACKGROUND = (100, 100, 100)  # (R, G, B)
COLOUR_RED        = (255,   0,   0)
COLOUR_GREEN      = (  0, 255,   0)
COLOUR_BUE        = (  0,   0, 255)
COLOUR_WHITE      = (255, 255, 255)

COLOURS = (COLOUR_RED, COLOUR_GREEN,COLOUR_BUE, COLOUR_WHITE )
colour = COLOUR_RED

"""
    Matrix with dymantions width, heigt to simulate a Neopixel display
    This version uses X, Y position, a neopixel matrix works with an index number.
"""
class pyMatrix():
    _oldPositions = []
    LINE_WIDTH 	  = 3
    MAX_PIXELS	  = 800
    
    """
        init function of the class
    """
    def __init__(self, width = 32, height = 16):
        #print(sysfont.get_fonts()[0])
        #self.font = pygame.font.SysFont(sysfont.get_fonts()[0], 25)
        self._maxX = width
        self._maxY = height
        self._squareSize       = min((self.MAX_PIXELS / self._maxX) - self.LINE_WIDTH * ((self.MAX_PIXELS + 1) / self.MAX_PIXELS),
                                     (self.MAX_PIXELS / self._maxY) - self.LINE_WIDTH * ((self.MAX_PIXELS + 1) / self.MAX_PIXELS))
        self._resolution 	  = ((self._squareSize + self.LINE_WIDTH) * self._maxX, (self._squareSize + self.LINE_WIDTH) * self._maxY)
        self._screen = pygame.display.set_mode(self._resolution)
        self._clock = pygame.time.Clock()  # to set max FPS
        pygame.display.set_caption('Neopixel matrix')
        self._drawScreen()
    
#     def showNeoPixelIndex(self):
#         for y in range(self._maxY):
#             for x in range(self._maxX):
#                 x, y = self._getPixelPos(posX, posY)
#                 geometry = (x, y, self._squareSize, self._squareSize)
#                 self._screen.blit(self.font.render('1', True, (255,255,255)), (200, 100))
#                 pygame.display.update()
    
    """
        return the width and height (in positions)  of the matrix
    """
    def getWidthHeight(self):
        return self._width, self._height
    
    """
        True if the PosX, posY is within the boundries of the matrix
    """
    def isPosAllowed(self, posX, posY):
        if posX < 0 or posY < 0:
            return False
        if posX >= self._maxX:
            return False
        if posY >= self._maxY:
            return False
        return True
    
    
    """
        position is a list of (row, col, color)
        if color is None, the background color is reset.
    """
    def drawGame(self, positions : list, colour = None):
        if set(positions) != set(self._oldPositions):
            self.drawGame (self._oldPositions,  COLOUR_BACKGROUND)        
        for x,y,c in positions:
            if colour == None:
                colour = c
            geometry = self._draw_square(x, y, colour)
            pygame.display.update(geometry)
        self._oldPositions = list(positions)



    """
        Check if quit event was raisen, if so quit the pyGame,
        You should end the program (quit()) 
    """
    def quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
        return False
    
    """
        Get the raisen events
    """
    def getEvents(self):
        self._clock.tick(60)  # max FPS = 60
        return pygame.event.get()
    
    """
        return the keys pressedc (ascii value)
    """
    def getPressedKey(self):
        keys = []
        for event in self.getEvents():
            if event.type == pygame.KEYDOWN:
                keys.append(event.key)
        return keys
          
    """ ----------------------- Private functions ------------------------- """
    
    """
        from the postion posX, posY calculate and return the position in pixels.
    """
    def _getPixelPos(self, posX, posY):
        return self.LINE_WIDTH * (posX + 1) + self._squareSize * posX, self.LINE_WIDTH * (posY + 1) + self._squareSize * posY

    """
        Draw a square on the PosX, PosY location with a given colod
    """
    def _draw_square(self, posX, posY, color = COLOUR_BACKGROUND):
        x, y = self._getPixelPos(posX, posY)
        geometry = (x, y, self._squareSize, self._squareSize)
        pygame.draw.rect(self._screen, color, geometry)
        return geometry
    
    
    """
        Dwaw all the squares on the screen
    """
    def _draw_squares(self):
        for y in range(self._maxY):
            for x in range(self._maxX):
                self._draw_square(x, y)            
    
    
    """
        Redraw the complete screen
    """
    def _drawScreen(self):
        self._screen.fill((0, 0, 0))  # Fill screen with black color.
        self._draw_squares()
        pygame.display.flip()  # Update the screen.


if __name__ == "__main__":
    posX  = 10
    posY  = 10
    moveX = 1
    moveY = 0
    color = (255,0,0)
    game = pyMatrix()
#     game.showNeoPixelIndex()
    speed = 10
    counter = 0
    while True:
        keys = game.getPressedKey()
        if pygame.K_q in keys:
            colour = random.choice(COLOURS)
        elif pygame.K_z in keys:
            moveY = 1
            moveX = 0
        elif pygame.K_w in keys:
            moveY = -1
            moveX = 0
        elif pygame.K_a in keys:
            moveY = 0
            moveX = -1
        elif pygame.K_s in keys:
            moveY = 0
            moveX = 1
        if counter % speed == 0:
            if game.isPosAllowed(posX + moveX, posY + moveY):
                posX += moveX
                posY += moveY
        positions =[(posX, posY, colour)]
        game.drawGame (positions )
        
        if game.quit():
            quit()
            
        counter += 1
