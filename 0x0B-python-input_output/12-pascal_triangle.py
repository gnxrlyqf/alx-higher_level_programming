#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """represent pascal triangle of size n

    returns list of list representing pascal's triangle
    """
    if n <= 0:
        return []
    triangle = [None] * n
    for i in range(n):
        triangle[i] = [None] * (i + 1)
        triangle[i][0] = 1
        triangle[i][len(triangle[i]) - 1] = 1
    for i in range(2, n):
        for j in range(1, len(triangle[i]) - 1):
            triangle[i][j] = triangle[i - 1][j] + triangle[i - 1][j - 1]

    return triangle
