#!/usr/bin/python3
"""
Module : Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """ 90 degrees clockwise rotation function
    Args:
        matrix (list[[list]]): a 2D matrix
    """
    mat = len(matrix)
    for i in range(int(mat / 2)):
        y = (mat - i - 1)
        for p in range(i, y):
            x = (mat - 1 - p)
            # start current number index
            temp = matrix[i][p]
            # switch the top for left
            matrix[i][p] = matrix[x][i]
            # switch the left for bottom
            matrix[x][i] = matrix[y][x]
            # switch the  bottom for right
            matrix[y][x] = matrix[p][y]
            # switch the right for top
            matrix[p][y] = temp
