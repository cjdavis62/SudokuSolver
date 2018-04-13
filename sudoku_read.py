import os
from sudoku_class import sudoku

def read_sudoku(filename):

    ### Read in text file with sudoku grid
    ### Example X from 0-9 (0 for empty slot):
    ### 
    ### X X X X X X X X X
    ### X X X X X X X X X
    ### X X X X X X X X X
    ### X X X X X X X X X
    ### X X X X X X X X X
    ### X X X X X X X X X
    ### X X X X X X X X X
    ### X X X X X X X X X
    ### X X X X X X X X X

    text_file = open(filename,"r") 
    sudoku_init = sudoku("init")
    i = 0
    for line in text_file:
        values = line.split(' ')
        j = 0
        for value in values:
            sudoku_init.change_value(int(values[j]), i, j)
            #print (values[j])
            j = j + 1
        i = i + 1

    return sudoku_init

new_sudoku = read_sudoku("sudoku_example.txt")
new_sudoku.show()
