import pygame
import game_snake as game

COLOUR_BACKGROUND = (100, 100, 100)  # (R, G, B)
COLOUR_RED        = (255,   0,   0)

class pyMatrix():
    _oldPositions = []
    LINE_WIDTH 	  = 3
    MAX_PIXELS	  = 800
    def __init__(self, width = 32, height = 16):
        self._maxX = width
        self._maxY = height
        self._squareSize       = min((self.MAX_PIXELS / self._maxX) - self.LINE_WIDTH * ((self.MAX_PIXELS + 1) / self.MAX_PIXELS),
                                     (self.MAX_PIXELS / self._maxY) - self.LINE_WIDTH * ((self.MAX_PIXELS + 1) / self.MAX_PIXELS))
        self._resolution 	  = ((self._squareSize + self.LINE_WIDTH) * self._maxX, (self._squareSize + self.LINE_WIDTH) * self._maxY)
        self._screen = pygame.display.set_mode(self._resolution)
        self._clock = pygame.time.Clock()  # to set max FPS
        self.drawScreen()
        
    def quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
        return False
                
    def getEvents(self):
        self._clock.tick(60)  # max FPS = 60
        return pygame.event.get()
    
    def getPressedKey(self):
        keys = []
        for event in self.getEvents():
            if event.type == pygame.KEYDOWN:
                keys.append(event.key)
        return keys
          
    def getPixelPos(self, x, y):
        return self.LINE_WIDTH * (x + 1) + self._squareSize * x, self.LINE_WIDTH * (y + 1) + self._squareSize * y

    def draw_square(self, posX, posY, color):
        x, y = self.getPixelPos(posX, posY)
        geometry = (x, y, self._squareSize, self._squareSize)
        pygame.draw.rect(self._screen, color, geometry)
        return geometry

    def draw_squares(self):
        for y in range(self._maxY):
            for x in range(self._maxX):
                self.draw_square(x, y, COLOUR_BACKGROUND)            

    def drawScreen(self):
        self._screen.fill((0, 0, 0))  # Fill screen with black color.
        self.draw_squares()
        pygame.display.flip()  # Update the screen.

    def getWidthHeight(self):
        return self._width, self._height
    
    def isPosAllowed(self, posX, posY):
        if posX < 0 or posY < 0:
            return False
        if posX >= self._maxX:
            return False
        if posY >= self._maxY:
            return False
        return True
    
    #position is a list of (row, col, color)
    #if color is None, the background color is reset.
    def drawGame(self, positions : list, colour = None):
        if set(positions) != set(self._oldPositions):
            self.drawGame (self._oldPositions,  COLOUR_BACKGROUND)        
        for x,y,c in positions:
            if colour == None:
                colour = c
            geometry = self.draw_square(x, y, colour)
            pygame.display.update(geometry)
        self._oldPositions = list(positions)

if __name__ == "__main__":
    posX  = 10
    posY  = 10
    moveX = 1
    moveY = 0
    color = (255,0,0)
    game = pyMatrix()
    speed = 10
    counter = 0
    while True:
        keys = game.getPressedKey()
        
        if pygame.K_z in keys:
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
        positions =[(posX, posY, COLOUR_RED)]
        game.drawGame (positions )
        
        if game.quit():
            quit()
            
        counter += 1
