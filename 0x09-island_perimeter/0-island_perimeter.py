#!/usr/bin/python3
"""
This module contains a function to calculate the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island defined by the grid.

    Args:
        grid (list of list of int): A grid where 1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Each land cell initially adds 4 to the perimeter
                perimeter += 4

                # If the left neighbor is land, subtract 2 (shared border)
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

                # If the upper neighbor is land, subtract 2 (shared border)
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

    return perimeter
