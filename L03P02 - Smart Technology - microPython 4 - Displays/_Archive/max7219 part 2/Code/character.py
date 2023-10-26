ARROW_U=((0,0,0,0,1,0,0,0),
         (0,0,0,1,1,1,0,0),
         (0,0,1,1,1,1,1,0),
         (0,1,1,1,1,1,1,1),
         (0,0,0,1,1,1,0,0),
         (0,0,0,1,1,1,0,0),
         (0,0,0,1,1,1,0,0),
         (0,0,0,0,0,0,0,0)
         )

ARROW_D=((0,0,0,1,1,1,0,0),
         (0,0,0,1,1,1,0,0),
         (0,0,0,1,1,1,0,0),
         (0,1,1,1,1,1,1,1),
         (0,0,1,1,1,1,1,0),
         (0,0,0,1,1,1,0,0),
         (0,0,0,0,1,0,0,0),
         (0,0,0,0,0,0,0,0)
         )

characters = {1 : ARROW_U,
              2 : ARROW_D
             }
#y <= 0
def getScrollingChar(character, y = 0):
    height = len(character)
    y = y % height
    for row in character[y:]:
        yield row
           
    for row in character[:y]:
        yield row
                
def _printCharacter(character):
    for row in character:
        for pixel in row:
            if pixel == 1:
                print("X", end="")
            else:
                print(" ", end="")
        print()
        
if __name__ == "__main__":
    print("--------------")
    for key in characters:
        _printCharacter(characters[key])
        print("--------------")
        
    print("--------------")
    for y in range(0, 9,1):
        _printCharacter(getScrollingChar(ARROW_U, y))
        print("--------------")
    
    print("--------------")
    for y in range(8,-5,-1):
        _printCharacter(getScrollingChar(ARROW_D, y))
        print("--------------")

