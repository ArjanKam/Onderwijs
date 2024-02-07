from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

_currentPos = 0
def move(pos):
    global _currentPos
    while _currentPos < pos:
        robotArm.moveRight()
        _currentPos += 1
    while _currentPos > pos:
        robotArm.moveLeft()
        _currentPos -= 1
    
def moveTo(start, end, number):
    while number > 0:
        move(start)
        robotArm.grab()
        move(end)
        robotArm.drop()
        number -= 1
    
# Jouw python instructies zet je vanaf hier:
for pos in (1,3,5,7,9):
    moveTo(pos,pos-1, 6)

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()