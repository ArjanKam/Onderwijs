from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

_currentPos = 0
def move(pos):
    global _currentPos
    while _currentPos < pos:
        robotArm.moveRight()
        _currentPos += 1
    while _currentPos > pos:
        robotArm.moveLeft()
        _currentPos -= 1
    
def moveTo(start, end):
    move(start)
    robotArm.grab()
    move(end)
    robotArm.drop()
    
# Jouw python instructies zet je vanaf hier:
blocks = 3
pos = 2
while blocks > 0:
    moveTo(0,pos)
    blocks -= 1
    pos += 1

blocks = 3
pos = 2
while blocks > 0:
    moveTo(pos,1)
    blocks -= 1
    pos += 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()