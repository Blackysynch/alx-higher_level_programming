#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        litt_matrix = []
        for j in i:
            j *= j
            litt_matrix.append(j)
        new_matrix.append(litt_matrix)
    return new_matrix
