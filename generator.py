# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 21:05:49 2020

@author: Kevin
"""

import random
import main
import copy

difficulty = 5-int(input("Select difficulty: Very Easy (0), Easy (1), Medium(2), Hard(3), Insane(4)"))
assert difficulty > 0 and difficulty <= 5, "Invalid entry"

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

initial = copy.deepcopy(board)


for cst1 in range(9):
    cst2 = 0    
    while cst2 != difficulty:
        randx = 3*(cst1%3)+random.randint(0,2)
        randy = 3*(cst1//3)+random.randint(0,2)
        if initial[randy][randx] != 0:
            continue
        rand_val = random.randint(1,9)
        board[randy][randx] = rand_val
        while not main.check_valid(board, randy, randx, rand_val):
            rand_val = random.randint(1,9)
            board = copy.deepcopy(initial)
            board[randy][randx] = rand_val
        while not main.solve(board):
            rand_val = random.randint(1,9)
            board = copy.deepcopy(initial)
            board[randy][randx] = rand_val
        initial[randy][randx] = rand_val
        board = copy.deepcopy(initial)
        cst2 += 1
        

                        