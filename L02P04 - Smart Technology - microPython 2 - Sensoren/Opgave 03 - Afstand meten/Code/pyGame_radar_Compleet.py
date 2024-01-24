import pygame
import math
import random
import serial
from time import sleep
# screen size
WIDTH, HEIGHT = 800, 600
# Radar settings
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT
DISTANCE_MAX = WIDTH // 2

data = (
(0,1125.7732),
(5,1142.6116),
(10,1125.7732),
(15,1117.5258),
(20,1117.182),
(25,999),
(30,1944.6734000000001),
(35,2326.116),
(40,2392.44),
(45,991.7525999999999),
(50,340.8934),
(55,331.27139999999997),
(60,331.27139999999997),
(65,999),
(70,1607.9038),
(75,1662.8865999999998),
(80,1511.6838000000002),
(85,1502.0618),
(90,1484.1924),
(95,1476.9758),
(100,1452.5774000000001),
(105,3067.698),
(110,3100.0),
(115,3075.602),
(120,3083.848),
(125,191.06529999999998),
(130,165.2921),
(135,164.26116000000002),
(140,181.09966),
(145,3068.384),
(150,1353.9518),
(155,999),
(160,2287.972),
(165,999),
(170,2904.812),
(175,999),
(175,999),
(170,999),
(165,1419.244),
(160,999),
(155,2441.238),
(150,999),
(145,173.88316),
(140,151.20274),
(135,179.0378),
(130,108.9347),
(125,115.80756),
(120,124.74226),
(115,999),
(110,142.61168),
(105,162.19930000000002),
(100,163.23024),
(95,1296.2200000000003),
(90,1262.5430000000001),
(85,1260.8248),
(80,1289.0034),
(75,1263.5738000000001),
(70,1278.3506),
(65,1285.9106),
(60,1326.1168),
(55,999),
(50,340.5498),
(45,340.2062),
(40,340.8934),
(35,1008.9348),
(30,983.5052000000001),
(25,1146.7354),
(20,1241.5808),
(15,1160.1374),
(10,1117.5258),
(5,1108.591),
(0,1125.4296)
)

# colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
DARKGREEN = (50, 100, 50)

BACKGROUND = DARKGREEN
SCANNER = RED
COLOR_OBJECT = WHITE

# import measureUltrasoon as ultrasoon
serial_port = 'COM17'
baud_rate   = 115200
ser = serial.Serial(serial_port, baud_rate)				# Create a serial object

# Initialise Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ultrasoon scanner")

_angle = 0
def readDistance():
    global _angle
    _angle += 5
    if _angle > 360:
        _angle = 0
    return _angle, random.randint(5, 4 * DISTANCE_MAX)

def readUltrasoon():
    data = ser.readline().decode('utf-8').strip() 	# Read a line from the serial port
    angle, distance = data.split(" ")
    angle = int(angle)
    distance = float(distance)
    distance *= 20
    if distance < 0:
        distance = 999
    return angle, distance

_index = 0
def readDummyData():
    global _index
    _index += 1
    if _index >= len(data):
        _index = 0
    sleep(0.2)
    return data[_index]  
    
    
def measure():
    angle, distance = readDummyData()   
#   angle, distance = readUltrasoon()   
#   angle, distance = readDistance()

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
    try:
        main()
    except KeyboardInterrupt:
        # Close the serial port when the program is interrupted (Ctrl+C)
        ser.close()
        print("Serial port closed.")
