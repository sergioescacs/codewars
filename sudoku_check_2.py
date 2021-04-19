#Sudoku Background

#Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells 
# of the grid with digits from 1 to 9, so that each column, each row, and each of the 
# nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.


#Sudoku Solution Validator

#Write a function that accepts a 2D array representing a Sudoku board, 
# and returns true if it is a valid solution, or false otherwise. The cells of the sudoku 
# board may also contain 0's, which will represent empty cells. Boards containing one or more 
# zeroes are considered to be invalid solutions.
#The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

#NOT FINISHED YET

def valid_solution(board):
    
    reverse = [[], [], [], [], [], [], [], [], []]
    
    for a in range(9):
        for b in range(9):
            reverse[a].append(board[b][a])           
    
    for c in range(9):
         for x in range(9):
            y = board[x][c]
            x = board[c][x]
            
            if board[c].count(x) > 1 or x == 0 or reverse[c].count(y) > 1 or y == 0:
                return False

    return True

print(valid_solution([[1, 2, 3, 4, 5, 6, 7, 8, 9], 
                    [2, 3, 4, 5, 6, 7, 8, 9, 1], 
                    [3, 4, 5, 6, 7, 8, 9, 1, 2], 
                    [4, 5, 6, 7, 8, 9, 1, 2, 3], 
                    [5, 6, 7, 8, 9, 1, 2, 3, 4], 
                    [6, 7, 8, 9, 1, 2, 3, 4, 5], 
                    [7, 8, 9, 1, 2, 3, 4, 5, 6], 
                    [8, 9, 1, 2, 3, 4, 5, 6, 7], 
                    [9, 1, 2, 3, 4, 5, 6, 7, 8]])) #False

