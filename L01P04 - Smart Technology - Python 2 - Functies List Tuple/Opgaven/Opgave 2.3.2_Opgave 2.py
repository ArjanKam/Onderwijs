from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

#pos : negative is move to left, positive is move ro right
def moveArm(pos):
    error = False
    while pos < 0:
        pos += 1
        robotArm.moveLeft()
    while pos > 0:
        pos -= 1
        robotArm.moveRight()
        
    if error == True:
        return False
    else:
        return True
    
def grapAndDrop(moveLeft, moveRight):
    moveArm(-moveLeft)
    robotArm.grab()
    moveArm(moveRight)
    robotArm.drop()

grapAndDrop(0,9)
grapAndDrop(5,5)
grapAndDrop(2,2)
robotArm.wait()