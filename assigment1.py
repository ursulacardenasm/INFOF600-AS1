# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 16:44:32 2023

@author: mathilde brusselmans and Ursula
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


def is_valid_sudoku(sudokufield):
    board = sudokufield[:]
    for line in sudokufield:
        line.sort()
        for i in range()
        
    def is_valid_line(line):
        return True
    def is_valid_square(square):
        return True
        
 board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]