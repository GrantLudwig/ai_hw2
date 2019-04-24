#hw2.py v2.0
#Grant Ludwig
#4/26/19

#Completes the queen problem

import sys

def buildBoard(size):
    board = []
    for i in range(0,size):
        list = []
        for j in range(0,size):
            list.append(False)
        board.append(list)
    return board

def printBoard(board):
    for row in board:
        rowStr = ''
        for spot in row:
            if spot:
                rowStr += 'X '
            else:
                rowStr += '_ '
        print(rowStr)

def goodBoard(board, row, col, numQueens):
    #Checks rows
    for c in range(col):
        if board[row][c]:
            return False
    #Checks lower diagonal to left
    #zip combines the 2 ranges, needed to increment at the same rate
    for i,j in zip(range(row, numQueens, 1),range(col, -1, -1)):
        if board[i][j]:
            return False
    #Checks upper diagonal to left
    #zip combines the 2 ranges, needed to increment at the same rate
    for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True

#places queens by columns
#col acts like the num of queens
def backSearch(board, col, numQueens):
    if col >= numQueens:
        return True
    for row in range(numQueens):
        if goodBoard(board, row, col, numQueens):
            board[row][col] = True
            if backSearch(board, col+1, numQueens):
                return True
            else:
                board[row][col] = False
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