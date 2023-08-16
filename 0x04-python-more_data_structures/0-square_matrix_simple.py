#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[value for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = matrix[i][j] * matrix[i][j]
    return new_matrix
