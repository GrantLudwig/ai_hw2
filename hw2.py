
import sys

def buildBoard(size):
    board = []
    for i in range(0,size):
        list = []
        for j in range(0,size):
            list.append(0)
        board.append(list)
    return board

def printBoard(board):
    for row in board:
        rowStr = ''
        for spot in row:
            rowStr += str(spot) + ' '
        print(rowStr)

def goodBoard(board, row, col, numQueens):
    #Checks rows
    for i in range(col):
        if board[row][i] == 1:
            return False
    #Checks lower diagonal on left side 
    for i,j in zip(range(row, numQueens, 1),range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    #Checks upper diagonal on left side
    for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def backSearch(board, col, numQueens):
    if col >= numQueens:
        return True
    for i in range(numQueens):
        if goodBoard(board, i, col, numQueens):
            board[i][col] = 1
            if backSearch(board, col+1, numQueens):
                return True
            else:
                board[i][col] = 0
    return False


#driver code
boardQueenAmount = sys.argv[1]
board = buildBoard(int(boardQueenAmount))
print('Starting board')
printBoard(board)
print('\n')
if backSearch(board, 0, int(boardQueenAmount)):
    print('Solution board')
    printBoard(board)
else:
    print('Solution does not exist')