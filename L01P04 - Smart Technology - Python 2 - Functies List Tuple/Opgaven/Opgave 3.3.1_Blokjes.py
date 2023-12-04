from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

def moveBlock(verplaats):
    while verplaats > 0:
        robotArm.moveRight()
        verplaats -= 1
    while verplaats < 0:
        robotArm.moveLeft()
        verplaats += 1

def grabAndDrop(moveBefore, moveAfter):
    moveBlock(moveBefore)
    robotArm.grab()
    moveBlock(moveAfter)
    robotArm.drop()
    
grabAndDrop(0,9)
grabAndDrop(-5,5)
grabAndDrop(-2,2)

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
