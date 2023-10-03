#!/usr/bin/python3
def matrix_divided(matrix, div):
	if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
		raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
	if not all(len(row) == len(matrix[0]) for row in matrix):
		raise TypeError("Each row of the matrix must have the same size")
	for row in matrix:
		for column in row:
			if not isinstance(column, int) and not isinstance(column, float):
				raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
	if not isinstance(div, float) and not isinstance(div, int):
		raise TypeError("div must be a number")
	if div == 0:
		raise ZeroDivisionError("division by zero")
	new_matrix = [row[:] for row in matrix]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			new_matrix[i][j] = round(matrix[i][j] / div, 2)
	return new_matrix
