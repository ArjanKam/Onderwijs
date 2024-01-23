import pygame
import math
import random

# import measureUltrasoon as ultrasoon

# screen size
WIDTH, HEIGHT = 800, 600
# Radar settings
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT
DISTANCE_MAX = WIDTH // 2

# colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
DARKGREEN = (50, 100, 50)

BACKGROUND = DARKGREEN
SCANNER = RED
COLOR_OBJECT = WHITE

_angle = 0

# Initialise Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ultrasoon scanner")


def readDistance():
    global _angle
    _angle += 5
    if _angle > 360:
        _angle = 0
    return _angle, random.randint(5, 4 * DISTANCE_MAX)


def measure():
    angle, distance = readDistance()
    print(angle, distance)
    return angle, distance


def get_x(angle, distance):
    return int(distance * math.cos(math.radians(angle)))


def get_y(angle, distance):
    return int(distance * math.sin(math.radians(angle)))  # Inverted Y-axis for correct display


def get_coordinate(angle, distance):
    x = CENTER_X + get_x(angle, distance)
    y = CENTER_Y - get_y(angle, distance)
    return x, y


# Functie om te controleren of objecten zich binnen het radarbereik bevinden
_objects = {}
_lastAngle_draw = 0
_oldAngle = 0


def check_objects():
    global _lastAngle_draw
    angle, distance = measure()

    angle2 = angle
    if angle2 > 180:
        angle2 = 360 - angle2
    if distance <= DISTANCE_MAX:
        _objects[angle2] = distance
    elif angle2 in _objects:
        del _objects[angle2]

    delta_angle = abs(_lastAngle_draw - angle2)
    _lastAngle_draw = angle2

    return angle, delta_angle


def draw_arc_line(point_center, angle, step, distance, color):
    point_1 = get_coordinate(angle - step / 2, distance)
    point_2 = get_coordinate(angle + step / 2, distance)
    pygame.draw.polygon(screen, color, (point_center, point_1, point_2))


def draw_scan_line(angle, step):
    global _oldAngle
    if angle > 180:
        angle = 360 - angle

    point_center = (CENTER_X, CENTER_Y)
    draw_arc_line(point_center, _oldAngle, step, DISTANCE_MAX, BACKGROUND)
    draw_arc_line(point_center, angle, step, DISTANCE_MAX, SCANNER)

    _oldAngle = angle


def draw_objects(color, step):
    for angle in _objects.keys():
        distance = _objects[angle]
        point_start = get_coordinate(angle, distance)
        pygame.draw.circle(screen, RED, point_start, 1)
        draw_arc_line(point_start, angle, step, DISTANCE_MAX, color)
    for radius in range(0, HEIGHT, 50):  # draw line each 50 pixels
        pygame.draw.circle(screen, GREEN, (CENTER_X, CENTER_Y), radius, 1)


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
        draw_scan_line(angle, step)  # draw line
        draw_objects(COLOR_OBJECT, step)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()


if __name__ == "__main__":
    main()
