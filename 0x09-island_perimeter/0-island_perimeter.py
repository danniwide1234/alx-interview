#!/usr/bin/python3
"""Check if the grid is empty"""


def island_perimeter(grid):
    """Check if the grid is empty"""
    if not grid:
        return 0

    # Get the dimensions of the grid
    num_rows, num_cols = len(grid), len(grid[0])

    # Initialize the perimeter to zero
    perimeter_length = 0

    # Loop over all cells in the grid
    for row in range(num_rows):
        for col in range(num_cols):
            # Check if the current cell is land
            if grid[row][col] == 1:
                # Check if the cell to the left is water or out of bounds
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter_length += 1
                # Check if the cell to the right is water or out of bounds
                if col == num_cols - 1 or grid[row][col + 1] == 0:
                    perimeter_length += 1
                # Check if the cell above is water or out of bounds
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter_length += 1
                # Check if the cell below is water or out of bounds
                if row == num_rows - 1 or grid[row + 1][col] == 0:
                    perimeter_length += 1

    return perimeter_length
