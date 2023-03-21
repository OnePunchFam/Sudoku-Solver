def find_empty_location(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None

def is_valid_location(grid, row, col, num):
    # Check if the same number exists in the same row
    for x in range(9):
        if grid[row][x] == num:
            return False
    # Check if the same number exists in the same column
    for x in range(9):
        if grid[x][col] == num:
            return False
    # Check if the same number exists in the same 3x3 box
    box_row = row - row % 3
    box_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[box_row + i][box_col + j] == num:
                return False
    return True

def solve_sudoku(grid):
    # Find an empty location to start with
    find = find_empty_location(grid)
    if not find:
        return True
    row, col = find
    # Try numbers from 1 to 9
    for num in range(1, 10):
        # Check if the number is valid in this location
        if is_valid_location(grid, row, col, num):
            grid[row][col] = num
            # Recursively try to solve the rest of the grid
            if solve_sudoku(grid):
                return True
            # If the solution is not possible, backtrack and try again with a different number
            grid[row][col] = 0
    return False

# Test the code
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 0, 0, 0, 2, 0],
        [9, 0, 0, 8, 0, 0, 0, 0, 5],
        [0, 5, 0, 0, 0, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

if solve_sudoku(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
else:
    print("No solution exists")