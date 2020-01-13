# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 21:05:49 2020

@author: Kevin
"""

def solve(board):
    if find_empty(board) == None:
        return True
    else:
        y, x = find_empty(board)

        for i in range(1,10):
            if check_valid(board, y, x, i):
                board[y][x] = i


                if solve(board):
                    return True

                board[y][x] = 0

        return False


#check if there are any empty cases, if not finish
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)
    return None

#check if element at position x, y is valid
def check_valid(board, y, x, element = 0):
    if element == 0:
        element = board[y][x]
    #check if number already in same line
    for i in range(len(board)):
        if i == x:
            continue
        elif board[y][i] == element:
            return False
    #check if number already in same column
    for j in range(len(board)):
        if j == y:
            continue
        elif board[j][x] == element:
            return False
    #check if number in the square
    start_x, start_y = (x//3)*3, (y//3)*3
    for j in range(start_y, start_y+3):
        for i in range(start_x, start_x+3):
            if i == x and j == y:
                continue
            elif board[j][i] == element:
                return False
    return True

#print the board in a sudoku format
def print_board(board):
    print("--------------------------")
    for m in range(len(board)):
        print("| ", end = '')
        for n in range(len(board)):
            print(board[m][n], end = ' ')
            if (n+1) % 3 == 0:
                if n == 8:
                    print("|")
                else:
                    print("| ", end = '')
        if (m+1) % 3 == 0:
            print("--------------------------")

#final check if correct
def check_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if not check_valid(board, i, j):
                print("Solving Failed")
                return False

    print("Solving Succeeded")
    return True

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]


if __name__ == '__main__':
    solve(board)
    print_board(board)
