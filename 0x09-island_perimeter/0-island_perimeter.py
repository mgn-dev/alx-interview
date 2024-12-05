#!/usr/bin/python3
"""
Module to calculate the perimeter of an island represented in a grid.

The grid consists of lists of integers where 1 represents land
and 0 represents water. The function `island_perimeter` computes
the perimeter of the island formed by land cells, ensuring no lakes
are present (water inside the island).

Functions:
    island_perimeter(grid): Returns the perimeter of the island.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.

    Parameters:
        grid (list of list of int): A rectangular grid
        representing water and land. 0 represents water
        and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    if not grid:
        return 0

    height = len(grid)
    width = len(grid[0])
    perimeter = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:  # Found land
                # Check all four sides
                # Up
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Down
                if i == height - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Right
                if j == width - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
