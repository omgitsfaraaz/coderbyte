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