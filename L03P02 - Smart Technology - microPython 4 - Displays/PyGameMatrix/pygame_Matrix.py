import pygame
import game

COLOUR_BACKGROUND = (100, 100, 100)  # (R, G, B)
COLOUR_SNAKE      = (0,0,255)
RESOLUTION 		  = (800, 800)
MAP_SIZE 		  = (16, 16)  # (rows, columns)
LINE_WIDTH 		  = 3
square_width  = (RESOLUTION[0] / MAP_SIZE[0]) - LINE_WIDTH * ((MAP_SIZE[0] + 1) / MAP_SIZE[0])
square_height = (RESOLUTION[1] / MAP_SIZE[1]) - LINE_WIDTH * ((MAP_SIZE[1] + 1) / MAP_SIZE[1])
    
screen = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()  # to set max FPS

def convert_column_to_x(column, square_width):
    return LINE_WIDTH * (column + 1) + square_width * column

def convert_row_to_y(row, square_height):
    return LINE_WIDTH * (row + 1) + square_height * row

def draw_square(row, column, color):
    x = convert_column_to_x(column, square_width)
    y = convert_row_to_y(row, square_height)
    geometry = (x, y, square_width, square_height)
    pygame.draw.rect(screen, color, geometry)
    return geometry

def draw_squares():
    for row in range(MAP_SIZE[0]):
        for column in range(MAP_SIZE[1]):
            draw_square(row, column, COLOUR_BACKGROUND)            

def drawScreen():
    screen.fill((0, 0, 0))  # Fill screen with black color.
    draw_squares()
    pygame.display.flip()  # Update the screen.
    
#position is a list of (row, col, color)
#if color is None, the background color is reset.
def drawGame(positions : list):
    for pos in positions:
        if pos[2] == None:
            colour = COLOUR_BACKGROUND
        else:
            colour = pos[2]
        geometry = draw_square(pos[0], pos[1], colour)
        pygame.display.update(geometry)

drawScreen()
while True:
    clock.tick(60)  # max FPS = 60
    
    events = pygame.event.get()
    drawGame (game.playGame(events) )
    
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()