# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]

incorrect6 = [[0,1,2], 
              [2,0,1], 
              [1,2,0]]

def check_sudoku_mine(sudo):
    c_sudo = [[0 for i in range(len(sudo))] for j in range(len(sudo))]
    
    for i, row in enumerate(sudo):
        if len(set(row)) < len(sudo): return False
        for j, col in enumerate(row):
            if type(col) != int: return False
            elif col > len(sudo) or col < 1: return False
            
            c_sudo[j][i] = col 
            
    for row in c_sudo:
        if len(set(row)) < len(c_sudo): return False

    return True


def check_sudoku(p):
    n = len(p) # extact size of grid
    digit = 1 # start with 1
    while digit <= n: # go through each digit
        i = 0
        while i < n: # go through each row and cloumn
            row_count, col_count, j = 0, 0, 0
            while j < n: # for each entry in ith row/column
                if p[i][j] == digit: # check row count
                    row_count += 1
                if p[j][i] == digit:
                    col_count += 1
                j += 1
            if row_count != 1 or col_count != 1:
                return False
            i += 1 # next row/column
        digit += 1 # next digit
    return True # nothing was wrong!

            
print check_sudoku(incorrect6)

#print check_sudoku(incorrect)
#>>> False

#print check_sudoku(correct)
#>>> True

#print check_sudoku(incorrect2)
#>>> False

#print check_sudoku(incorrect3)
#>>> False

#print check_sudoku(incorrect4)
#>>> False

#print check_sudoku(incorrect5)
#>>> False


                
