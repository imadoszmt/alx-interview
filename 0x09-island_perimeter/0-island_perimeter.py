#!/usr/bin/python3
"""
Island Perimeter Module
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.

    Args:
        grid (list): A 2D list of integers where 0 represents water
        and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Check top
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # Check bottom
                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                # Check left
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # Check right
                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

    return perimeter


if __name__ == "__main__":
    island_perimeter(grid)
