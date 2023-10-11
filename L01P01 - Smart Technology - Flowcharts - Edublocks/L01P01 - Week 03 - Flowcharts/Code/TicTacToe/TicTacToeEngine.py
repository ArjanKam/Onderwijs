"""
    Tic Tac Toe
    Er is een manier om te winnen tegen de computer :)
"""

# Is het midden beschikbaar, is een hoek beschikbaar, is een zijkant beschikbaar
BEST_MOVES = [[1,1],[0,0],[2,2],[2,0],[0,2],[0,1],[1,0],[1,2],[2,1]]

"""
    Return a matrix of a board with the dimensions of size x size
    e,g, size = 3
    returns : [ [None, None, None], [None, None, None], [None, None, None] ]
    The board is a list of lists. board= [ [00, 01, 02], [10, 11, 12], [20, 21, 22] ]
        00  01  02
        10  11  12
        20  21  22
    board[1][0] = 10
    board[2][1] = 21
    
    x[y][x] 
"""

def getEmptyBoard(size = 3):
    return [[None]*size for i in range(size)]

"""
    Is the given position with posX and posY empy on the board (value is None)
"""
def isPositionEmpty(board, posX, posY):
    return getPiece(board, posX, posY) == None

"""
    Get the piece at the positon [posX], [posY] on the given [board]
"""
def getPiece(board, posX, posY):
    size = len(board)
    if posX < 0 or posX >= size: #controleer of de [posX] binnen de grenzen ligt
        raise Exception('Location not valid')
    if posY < 0 or posY >= size: #controleer of de [posY] binnen de grenzen ligt
        raise Exception('Location not valid')
    return board[posY][posX]

"""
    Set a [piece] on the positon [posX], [posY] on the given [board]
"""
def setPiece(board, posX, posY, piece, force = False):
    if not force and not isPositionEmpty(board, posX, posY):
        raise Exception('Location already occupied by a piece')
    board[posY][posX] = piece

"""
   Set a [piece] on the positon [pos] on the given [board]
   pos = (x,y)
"""
def setPiecePos(board, pos, piece):
    setPiece(board, pos[0], pos[1], piece)
    
"""
    returns the number of empty positions left on the [board]
"""
def getNumberEmptyPositions(board):
    count = 0
    for y in board:
        for x in y:
            if x == None:
                count += 1
    return count

"""
    returns if there is a winning position on the board (boad is 3x3)
"""
def hasWinner(board):
    size = len(board[0])
    # check if there is a winner on the horizontels
    for y in board:
        first = y[0]
        if first != None:
            for x in y:
                if first != x:
                    break
            else:
                return first
            
    #Check if there us a winner on the verticals
    #[ [1, 0, 0], [1, N, N], [1, 0, 0]]
    for x in range(0, size):
        first = board[0][x]
        if first == None:
            continue
        for y in range(1, size):
            if first != board[y][x]:
                break
        else:
            return first
        
    #check for diagonal left-right
    first = board[0][0]
    if first != None:
        for x in range(1, size):
            if first != board[x][x]:
                break
        else:
            return first
    
    #check for diagonal right-left
    first = board[0][size-1]
    if first != None:
        y = 0
        x = size-1
        for i in range(1, size):
            if first != board[y + i][x - i]:
                break
        else:
            return first
            
    return None

"""
    set [piece] on every position that has None at this moment on the [board]
    and check if this situation is a winning move
"""
def getWinningMove(board, piece):
    size = len(board)
    for y in range(size):
        for x in range(size):
            if not isPositionEmpty(board, x, y): 
               continue # if there is a piece on the location, continue
            setPiece(board, x, y, piece)  # set a piece on the None location
            winner = hasWinner(board)
            setPiece(board, x, y, None, True)   # Return the origional situation
            if winner == piece:
               return x,y
    return None

"""
    board with dimensions 3x3
    piece is your own piece
    other is piece of other party
"""
def getBestPosition(board, piece, other):
    # is er een plek die winst geeft?
    pos = getWinningMove(board, piece)
    if pos != None:
        return pos
    
    # other has clear winner
    pos = getWinningMove(board, other)
    if pos != None:
        return pos
    
    # Is het midden beschikbaar
    for y,x in BEST_MOVES:
        if board[y][x] == None:
            return (x,y)
    return None

"""
    Tests pn the TicTacToe Engine
"""
if __name__ == "__main__":
    try:
        assert(getPiece ([[1, 0, 1], [1, None, 0], [1, None, None]], -1, 0) == 0 )
        assert(False)
    except:
        assert(True) # raise Exception('Location not valid') was executed because -1 is not valid
        
    assert(getPiece ([[1, 0, 1], [1, None, 0], [1, None, None]], 1, 0) == 0 ) 
    assert(hasWinner([[1, 0, 1], [1, None, 0], [1, None, None]]) == 1), "Vertical winner 0"
    assert(hasWinner([[1, 0, 1], [None, 0, None], [None, 0, None]]) == 0), "Vertical winner 1"
    assert(hasWinner([[1, 0, 1], [None, None, 1], [None, 0, 1]]) == 1), "Vertical winner 2"
   
    assert(hasWinner([[1, 1, 1], [None, None, None], [None, None, None]]) == 1), "Horizontal winner 0"
    assert(hasWinner([[None, None, None], [1, 1, 1], [None, None, None]]) == 1), "Horizontal winner 1"
    assert(hasWinner([[None, None, None], [None, None, None], [1, 1, 1]]) == 1), "Horizontal winner 2"
     
    assert(hasWinner([[1, 0, 0], [0, 1, None], [0, None, 1]]) == 1), "Diagonal winner"
    assert(hasWinner([[1, 1, 0], [0, 0, None], [0, 1, None]]) == 0), "Diagonal winner"
     
    assert(hasWinner([[1, 0, 1], [0, None, None], [1, 0, None]]) == None), "No winner"

    assert(getWinningMove([[None, None, None], [1, None, 1], [None, None, None]], 1) == (1,1))
    assert(getWinningMove([[0, None, 1], [1, 0, 1], [None, None, None]], 1) == (2,2))
    assert(getWinningMove([[1, None, 1], [None, None, None], [None, None, None]], 1) == (1,0))
    
    assert(getBestPosition([[None, None, None], [None, 1, None], [None, 1, None]], 1, 0) == (1,0)), "Best position is to win (0,1)"
    assert(getBestPosition([[None, None, None], [None, 0, None], [None, None, 0]], 1, 0) == (0,0)),  "Best position is to win (0,0)"
    assert(getBestPosition([[0, None, 0], [None, None, None], [None, None, None]], 0, 1) == (1,0)), "Best position is to win (0,1)"
   
    assert(getNumberEmptyPositions([[0, None, 0], [1, 0, 1], [None, 1, None]]) == 3), "Three empty positions left"
