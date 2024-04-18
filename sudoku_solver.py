# helper functions to print the grid
def printGrid():
    for row in grid:
        print(row)

# Form the puzzle Grid
def form_grid(puzzle_string):
    global grid 
    print("The Sudoku Challenge")
    for i in range (0, len(puzzle_string), 9):
        row = puzzle_string[i:i+9]
        temp = []
        for block in row:
            temp.append(int(block))
        grid.append(temp)
    printGrid()

#Function to check if a digit can be placed in the given block
def possible(row,col,digit):
    global grid
    for i in range(0,9):
        if grid[row][i] == digit:
            return False
    for i in range(0,9):
        if grid[i][col] == digit:
            return False
    square_row = (row//3)*3
    square_col = (col//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[square_row+i][square_col+j] == digit:
                return False    
    return True

#traverse through all blocks w/ backtracking
def solve():
    global grid
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for digit in range(1,10):
                    if possible(row,col,digit):
                        grid[row][col] = digit
                        solve()
                        grid[row][col] = 0  #Backtrack step
                return
    print('\nThe Solution')
    printGrid()

#pass the Grid and Call the function to solve the puzzle
puzzle_string = "004300209005009001070060043006002087190007400050083000600000105003508690042910300"
grid = []
form_grid(puzzle_string)
solve()
