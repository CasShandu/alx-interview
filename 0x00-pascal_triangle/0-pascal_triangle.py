#!/usr/bin/python3
"""
This module provides a function to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Args:
        n (int): Number of rows of Pascal's Triangle to generate.

    Returns:
        list of lists of int: A list of lists representing Pascal's Triangle.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
