import TicTacToeEngine
import random, sys
sys.path.insert(1, '..')
import GameHelper

RANDOM_START = [(0,0), (2,0), (0,2), (2,2), (1,1)]
PIECES = ["X", "O"]

piece_width = 200
screen = GameHelper.initImageScreen(r'.//TTT_Board.jpg', caption="Boter, Kaas en eieren")
images = {"X": GameHelper.loadImage(r'.//TTT_X.jpg', piece_width, piece_width),
              "O": GameHelper.loadImage(r'.//TTT_O.jpg', piece_width, piece_width)
              }
font = GameHelper.pygame.font.Font('freesansbold.ttf',80)

def calculatePos(pos):
    return GameHelper.convertPosition((pos[0] * 300, pos[1] * 300 ))

"""
264, 270
514, 521
"""
def calculateXY(pos):
    #print(pos)
    x = 0
    if pos[0] < GameHelper.convert(264):
        x = 0
    elif pos[0] > GameHelper.convert(514):
        x = 2
    else:
        x = 1
    
    if pos[1] < GameHelper.convert(270):
        y = 0
    elif pos[1] > GameHelper.convert(521):
        y = 2
    else:
        y = 1
    
    return x, y
    

"""
other can be deleted after implementing mouse click
"""
def getCoordinate(board = None):
    while True:
        pos = GameHelper.getMousePressed()
        if pos == None:
            continue
        x, y = calculateXY(pos)
        if board == None or TicTacToeEngine.isPositionEmpty(board, x, y):
            return x,y
    return None
        
def setAnswers(pos, piece ):
    screen_pos = calculatePos(pos)
    GameHelper.drawImage(images[piece], screen_pos)
    GameHelper.refresh()
    
def game():
    board = TicTacToeEngine.getEmptyBoard()
    move = 0
    youStart = random.randint(1, 1000) % 2 == 0
    if not youStart:
        start = random.choice( RANDOM_START)
        TicTacToeEngine.setPiecePos(board, start, PIECES[1])
        setAnswers(start, PIECES[1])
        youStart = True
    while not TicTacToeEngine.hasWinner(board) and TicTacToeEngine.getNumberEmptyPositions(board) > 0:
        piece = PIECES[move % 2]
        other = PIECES[(1 + move) % 2]
        if youStart:
            best = getCoordinate(board)            
        else:
            best = TicTacToeEngine.getBestPosition(board, piece, other)
        TicTacToeEngine.setPiecePos(board, best, piece)
        setAnswers(best, piece)
        move += 1
        youStart = not youStart    
    return TicTacToeEngine.hasWinner(board)

if __name__ == "__main__":
    while True:        
        winner = game()
        text = "Gelijk spel"
        if winner != None:
            text = "{} heeft gewonnen".format(winner)
        GameHelper.drawText(text, GameHelper.convertPosition((400, 400)), font, GameHelper.COLOR_RED)
        GameHelper.refresh()
        best = getCoordinate()
        #GameHelper.getKeyPressed('\x20')        
        GameHelper.refreshImage()