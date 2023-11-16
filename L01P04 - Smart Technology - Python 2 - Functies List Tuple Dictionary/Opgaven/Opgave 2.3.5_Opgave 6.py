from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

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
blocks = 8
pos = 7
while blocks > 0:
    moveTo(pos,pos+1)
    blocks -= 1
    pos -= 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()