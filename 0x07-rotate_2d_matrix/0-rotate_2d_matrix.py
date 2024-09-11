#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """rotate two dimension matrix 90 degrees clockwise
    Args:
        matrix (list[[list]]): a matrix
    """
    size = len(matrix)
    for layer in range(int(size / 2)):
        end = (size - layer - 1)
        for element in range(layer, end):
            opposite = (size - 1 - element)
            # current number
            temp = matrix[layer][element]
            # change top for left
            matrix[layer][element] = matrix[opposite][layer]
            # change left for bottom
            matrix[opposite][layer] = matrix[end][opposite]
            # change bottom for right
            matrix[end][opposite] = matrix[element][end]
            # change right for top
            matrix[element][end] = temp
