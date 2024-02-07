import pygame
import game_snake as game

COLOUR_BACKGROUND = (100, 100, 100)  # (R, G, B)

MAX_X 		  = 32
MAX_Y		  = 16 
LINE_WIDTH 	  = 3
MAX_PIXELS	  = 800
SQUARE_SIZE       = min((MAX_PIXELS / MAX_X) - LINE_WIDTH * ((MAX_PIXELS + 1) / MAX_PIXELS), (MAX_PIXELS / MAX_Y) - LINE_WIDTH * ((MAX_PIXELS + 1) / MAX_PIXELS))
RESOLUTION 		  = ((SQUARE_SIZE + LINE_WIDTH) * MAX_X, (SQUARE_SIZE + LINE_WIDTH) * MAX_Y)

screen = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()  # to set max FPS

def getPixelPos(x, y):
    return LINE_WIDTH * (x + 1) + SQUARE_SIZE * x, LINE_WIDTH * (y + 1) + SQUARE_SIZE * y

def draw_square(posX, posY, color):
    x, y = getPixelPos(posX, posY)
    geometry = (x, y, SQUARE_SIZE, SQUARE_SIZE)
    pygame.draw.rect(screen, color, geometry)
    return geometry

def draw_squares():
    for y in range(MAX_Y):
        for x in range(MAX_X):
            draw_square(x, y, COLOUR_BACKGROUND)            

def drawScreen():
    screen.fill((0, 0, 0))  # Fill screen with black color.
    draw_squares()
    pygame.display.flip()  # Update the screen.

def isPosAllowed(posX, posY):
    if posX < 0 or posY < 0:
        return False
    if posX >= MAX_X:
        return False
    if posY >= MAX_Y:
        return False
    return True
    
#position is a list of (row, col, color)
#if color is None, the background color is reset.
def drawGame(positions : list, colour = None):
    for x,y,c in positions:
        if colour == None:
            colour = c
        geometry = draw_square(x, y, colour)
        pygame.display.update(geometry)

pygame.event.set_allowed((pygame.QUIT))
drawScreen()
oldPositions = []
while True:
    clock.tick(60)  # max FPS = 60
    
    events = pygame.event.get()
    positions = game.playGame(events, isPosAllowed)
    if set(positions) != set(oldPositions):
        drawGame (oldPositions,  COLOUR_BACKGROUND)
        drawGame (positions )
        oldPositions = list(positions)
    
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
            