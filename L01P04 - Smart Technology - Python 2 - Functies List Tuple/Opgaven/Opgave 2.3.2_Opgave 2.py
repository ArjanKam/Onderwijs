from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

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
moveTo(0,9)
moveTo(4,9)
moveTo(7,9)

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()