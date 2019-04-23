
import sys

def buildBoard(size):
    board = []
    for i in range(0,size):
        board.append([False, False, False])
    return board

def buildKnown(size):
    board = []
    for i in range(0,size):
        board.append([True, True, True])
    return board
   
def printBoard(board):
    for row in board:
        rowStr = '|'
        underStr = '_'
        for spot in row:
            rowStr += str(spot) + '|'
            underStr += '______'
        print(rowStr)
        print(underStr)


#driver code
boardQueenAmount = sys.argv[1]
board = buildBoard(int(boardQueenAmount))
print(board, '\n')
printBoard(board)