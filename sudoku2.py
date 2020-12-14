# Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with numbers in
# such a way that each column, each row, and each of the nine 3 × 3 sub-grids that compose
# the grid all contain all of the numbers from 1 to 9 one time.

# Implement an algorithm that will check whether the given grid of numbers represents a valid
# Sudoku puzzle according to the layout rules described above. Note that the puzzle
# represented by grid does not have to be solvable.

# For

# grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
#         ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
#         ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
#         ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
#         ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
#         ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
#         ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

# the output should be
# sudoku2(grid) = true;

# For

# grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
#         ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
#         ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
#         ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
#         ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
#         ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
#         ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
#         ['.', '2', '.', '.', '3', '.', '.', '.', '.']]

# the output should be
# sudoku2(grid) = false.

# The given grid is not correct because there are two 1s in the second column.
# Each column, each row, and each 3 × 3 subgrid can only contain the numbers 1
# through 9 one time.

def sudoku2(grid):
    row, col, block = set(), set(), set()
    for i in range(9):
        for j in range(9):
            if grid[i][j] != '.':
                r_key = (i, grid[i][j])
                c_key = (j, grid[i][j])
                b_key = (i//3, j//3, grid[i][j])
                if (r_key in row) or (c_key in col) or (b_key in block):
                    return False

                row.add(r_key)
                col.add(c_key)
                block.add(b_key)

    return True