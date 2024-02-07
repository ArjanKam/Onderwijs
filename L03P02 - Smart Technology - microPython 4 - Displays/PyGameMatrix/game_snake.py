import pygame
import time
COLOUR_RED        = (255,   0,   0)

lastTime = time.time()
moveDirection = [1,0]
posX = 10
posY = 10
def playGame(events, isPosAllowed = None):
    global posX, posY
    for event in events:
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_z:
            if isPosAllowed == None or isPosAllowed(posX, posY + 1):
                posY += 1
          elif event.key == pygame.K_w:
            if isPosAllowed == None or isPosAllowed(posX, posY - 1):
                posY -= 1
          elif event.key == pygame.K_a:
            if isPosAllowed == None or isPosAllowed(posX - 1, posY):
                posX -= 1
          elif event.key == pygame.K_s:
            if isPosAllowed == None or isPosAllowed(posX + 1, posY):
                posX += 1
    return [(posX, posY, COLOUR_RED)]
    
    
