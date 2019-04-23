
import sys

def buildBoard(size):
    board = []
    for i in range(0,size):
        board.append([False, False, False, False])
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

def colCheck(board):
    attack = False
    position = []
    for row in board:
        for colNum in range(len(row)):
            if row[colNum]:
                if colNum in position:
                    attack = True
                position.append(colNum)
    return attack

def diagcheck(board):
    attack = False
    return attack

def goodBoard(board):
    attack = colCheck(board)
    if not attack:
        attack = diagcheck(board)
    
    return attack

#driver code
boardQueenAmount = sys.argv[1]
board = buildBoard(int(boardQueenAmount))
print(board, '\n')
printBoard(board)
print('\n')
board = [[True, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, True]]
printBoard(board)
print('\n')
print(goodBoard(board))