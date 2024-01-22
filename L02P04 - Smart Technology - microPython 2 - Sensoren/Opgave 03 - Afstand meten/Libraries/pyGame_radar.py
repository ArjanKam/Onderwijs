import pygame
import math
import random
#import measureUltrasoon as ultrasoon

# Schermgrootte
WIDTH, HEIGHT = 800, 600
SCAN_DEGREES = 1  # Scan per hoek van 5 graden
# Radarinstellingen
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT
DISTANCE_MAX = WIDTH // 2

# Kleuren
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0,255,0)
DARKGREEN = (50,100,50)

BACKGROUND   = DARKGREEN
SCANNER      = RED
COLOR_OBJECT = WHITE

# Initialiseren van Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ultrasoon scanner")

_angle = 0
def measure():
    global _angle
    #data = ultrasoon.readDistance()
    hoek, afstand = (_angle, random.randint(5, 75) * DISTANCE_MAX / 75)
    print(hoek, afstand)
    _angle += 5
    if _angle > 360:
        _angle = 0
    return hoek, afstand * DISTANCE_MAX / 75 

def getX(angle, distance):
    return int(distance * math.cos(math.radians(angle)))

def getY(angle, distance):
    return int(distance * math.sin(math.radians(angle)))  # Inverted Y-axis for correct display

def getCoordinate(angle, distance):
    x = CENTER_X + getX(angle, distance) 
    y = CENTER_Y - getY(angle, distance)
    return x,y  
        
# Functie om te controleren of objecten zich binnen het radarbereik bevinden
_objects = {}
def check_objects(): 
    angle, distance = measure()
    angle2 = angle
    if angle2 > 180:
        angle2 = 360-angle2
    if distance <= DISTANCE_MAX:
        _objects[angle2] = distance
    elif angle2 in _objects:
        del _objects[angle2]
    return angle, 1

def drawArcLine(point_center, angle, step, distance, color ):
    point_1 = getCoordinate(angle - step/2, distance)
    point_2 = getCoordinate(angle + step/2, distance)
    pygame.draw.polygon(screen, color, (point_center, point_1, point_2))
    
_oldAngle = 0
def drawScanLine(angle, step):
    global _oldAngle
    if angle > 180:
        angle = 360 - angle
        
    point_center = (CENTER_X, CENTER_Y)
    drawArcLine(point_center, _oldAngle, step, DISTANCE_MAX, BACKGROUND)
    drawArcLine(point_center,     angle, step, DISTANCE_MAX, SCANNER)
    
    _oldAngle = angle

def drawObjects(color, step):
    for angle in _objects.keys():
        distance = _objects[angle]
        point_start = getCoordinate(angle, distance)
        point_end   = getCoordinate(angle, DISTANCE_MAX)
        #pygame.draw.circle(screen, RED, point_start, 1)
        #pygame.draw.line  (screen, color, point_start, point_end)
        drawArcLine(point_start, angle, step, DISTANCE_MAX, color)
        
# Hoofdprogramma
def main():
    running = True
    clock = pygame.time.Clock()
    screen.fill(BACKGROUND)
    angle = 0
    objects = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        angle, step = check_objects()
        
        drawScanLine(angle, step) # Teken lijn van de scankop    
        drawObjects(COLOR_OBJECT, step)

        pygame.display.flip()
        clock.tick(30)

        #angle += SCAN_DEGREES
        #angle = angle % 360
        
    pygame.quit()

if __name__ == "__main__":
    main()
