# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 16:44:32 2023

@author: mathilde brusselmans and Ursula
"""
"""
Exercise 1
"""

def the_sequence(sequence_length, sequence_0 = ['1']):
    """
    
    """
    if len(sequence_0) >= sequence_length:
        return sequence_0  
    
    def generate_next_term(last_term):
        """generates the next term based on a given term, For example, if the 
        current term is 111221, the next term reads out the current term as 
        “three 1s, two 2s, one 1”, and thus the next term becomes 312211.
        """
        new_term = 0
        count = int(1)
        for i in range(0, len(last_term)-1):
            if last_term[i] == last_term[i+1]:
               count += 1
            else:
                new_term = new_term*100 + 10*count + int(last_term[i])
                #reset start conditions loop
                count = 1
        #add last unique number, '1' is taken into account     
        new_term = new_term*100 + 10*count + int(last_term[-1])            
        return str(int(new_term))
    sequence_1 = sequence_0 + [generate_next_term(sequence_0[-1])]       
    return the_sequence(sequence_length, sequence_0 = sequence_1)
    


print(the_sequence(2))
print(the_sequence(6))

"""
Exercise 1
"""

def is_valid_sudoku(sudoku):
    """
    This function checks if a sudoku board is valid
    """
    board = sudoku[:]

    #check if the values are between 1 and 9
    for row in board:
        for col in row:
            if col != '.':
                if int(col) > 9 or int(col) < 1:
                    return False

    #check if there are not repeated values in the columns and rows

    def check_columns(board): # this checks if there are duplicates in the columns
        for i in range(9): 
            element = []
            for row in board:
                if row[i] != '.':
                    element.append(row[i]) #append all values in rows to a list
            if len(element) != len(set(element)):
                return False
        return True
    
    def check_rows(board): #this checks if there are duplicates in the rows
        for i in range(9):
            element=[]
            for col in board[i]:
                if col != '.':
                    element.append(col) #append all values in columns to a list
            if len(element) != len(set(element)):
                return False
        return True
            
    def make_box(board, n_row, n_col): #this checks if there are duplices in the boxes
        box=[]
        for i in range(3):
            for j in range(3):
                box.append(board[n_row + i][n_col + j]) #this creates a list of the elements in the box
        element=[]
        for e in box:
            if e != '.':
                element.append(e)
        if len(element) != len(set(element)):
                return False
        return True
    
    if not check_columns(board): #if there are not duplicates in columns
        return False
    
    if not check_rows(board): #if there are not duplicates in rows
        return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not make_box(board,i,j):
                return False
    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

is_valid_sudoku(board)


board2 = [["9", "2", "6", "1", ".", ".", "3", "4", "."],
    ["8", "5", ".", "9", "4", "3", ".", "2", "6"],
    ["4", ".", ".", "6", ".", "2", ".", ".", "."],
    ["6", ".", ".", "2", "3", ".", "4", ".", "9"],
    [".", ".", "4", "8", ".", ".", ".", "6", "2"],
    ["2", ".", ".", "4", "6", "7", "5", "3", "."],
    [".", "6", ".", "7", ".", "4", ".", "1", "."],
    [".", "4", "2", "5", ".", ".", "6", ".", "."],
    ["1", ".", ".", "3", ".", "6", ".", "5", "4"]
]

is_valid_sudoku(board2)

board3 = [["7", "2", "6", "1", ".", ".", "3", "4", "."],
    ["8", "5", ".", "a", "4", "3", ".", "2", "6"],
    ["4", ".", ".", "6", ".", "2", ".", ".", "."],
    ["6", ".", ".", "2", "3", ".", "4", ".", "9"],
    [".", ".", "4", "10", ".", ".", ".", "6", "2"],
    ["2", ".", ".", "4", "6", "7", "5", "2", "."],
    [".", "6", ".", "7", ".", "4", ".", "9", "1"],
    [".", "4", "2", "5", ".", ".", ".", ".", "."],
    ["1", ".", ".", "3", ".", "6", ".", "5", "4"]
]

is_valid_sudoku(board3)

"""
Exercise 3
"""

def wins(board, charact):
    """
    This function checks if the character X or O wins
    """
    for i in range(3): #check rows
        if board[i][0] == board[i][1] == board[i][2] == charact:
            return True
    
    for i in range(3): #check columns
        if board[0][i] == board[1][i] == board[2][i] == charact:
            return True
    
    #check diagonals
    if board[0][0] == board[1][1] == board[2][2] == charact:
        return True
    if board[0][2] == board[1][1] == board[2][0] == charact:
        return True
    
    return False


def is_valid_tictactoe(total):
    """
    This function defines if the sudoku board is valid
    """
    
    #Conditions:
    #a)The lenght of the board must be 3
    if len(total) != 3:
        return False
    #b)The lenght of each row must be 3
    for row in total:
        if len(row) != 3:
            return False
    #c)There must be only 'X' and 'O' in the board
    for row in total:
        for col in row:
            if col != 'X' and col != 'O' and col != ' ':
                return False


    c_X = 0 #counting number of x's
    c_O = 0 #counting number of o's
    
    for row in total:
        for col in row:
            if col == 'X':
                c_X += 1
            elif col == 'O':
                c_O += 1
    
    #since X makes the first move, the count of X has to be equal or larger than O
    if c_O > c_X: 
        return False
    #if the difference between the number of X and O is larger than 1, then it is not valid
    if c_X - c_O > 1:
        return False

    #check win conditions
    x_wins = wins(total, 'X')
    o_wins = wins(total, 'O')

    #if X wins, then O cannot win
    if x_wins and o_wins:
        return False
    
    #if O wins, then the amount of X and O must be equal
    if o_wins and c_X != c_O:
        return False
    
    #if X wins, then the amount of X must be larger than O
    if x_wins and c_X <= c_O:
        return False

    return True

is_valid_tictactoe(["OOX","XXO","OXO"])
is_valid_tictactoe(["XOX"," X "," "])
is_valid_tictactoe(["XOX","O O","XOX"])


