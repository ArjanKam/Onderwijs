import TicTacToeEngine
import random
RANDOM_START = [(0,0), (2,0), (0,2), (2,2), (1,1)]

PIECES = ["X", "O"]
"""
"""
def showBoard(board):
    print("-" * 13)
    for y in board:
        print("|", end = "")
        for x in y:
            if x == None:
                print("{:3}|".format(''), end= "")
            else:
                print("{:^3}|".format(x), end= "")
        print()
        print("-" * 13)

def getCoordinate(board, piece):
    while True:
        position = input("Geef de coordinaten van je stuk [{}] in x,y :".format(piece))
        position = position.split(',')
        if len(position) != 2:
            continue
        try:
            x = int(position[0])
            y = int(position[1])
            if TicTacToeEngine.isPositionEmpty(board, x, y):
                return x,y
        except:
            print("Not valid coordinate")
            continue
            
def game():
    board = TicTacToeEngine.getEmptyBoard()
    move = 0
    youStart = random.randint(1, 1000) % 2 == 0
    if not youStart:
        start = random.choice( RANDOM_START)
        TicTacToeEngine.setPiecePos(board, start, PIECES[1])
        showBoard(board)
        youStart = True
    while not TicTacToeEngine.hasWinner(board) and TicTacToeEngine.getNumberEmptyPositions(board) > 0:
        piece = PIECES[move % 2]
        other = PIECES[(1 + move) % 2]
        if youStart:
            best = getCoordinate(board, piece)
        else:
            best = TicTacToeEngine.getBestPosition(board, piece, other)
        TicTacToeEngine.setPiecePos(board, best, piece)
        showBoard(board)
        move += 1
        youStart = not youStart
    return TicTacToeEngine.hasWinner(board)
    
def autoGame():
    board = TicTacToeEngine.getEmptyBoard()
    start = random.choice( RANDOM_START)
    TicTacToeEngine.setPiecePos(board, start, PIECES[1])
    showBoard(board)
    move = 0
    hasWinner = False
    while not TicTacToeEngine.hasWinner(board) and TicTacToeEngine.getNumberEmptyPositions(board) > 0:
        piece = PIECES[move % 2]
        other = PIECES[(1 + move) % 2]
        best = TicTacToeEngine.getBestPosition(board, piece, other)
        TicTacToeEngine.setPiecePos(board, best, piece)
        showBoard(board)
        move += 1
    return TicTacToeEngine.hasWinner(board)

if __name__ == "__main__":
    hasWinner = False
    while not hasWinner:
        print("------ NEW GAME -------")
        hasWinner = game()
        
     
