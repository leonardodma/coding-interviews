from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_copy = [row[:] for row in matrix]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j] = matrix_copy[len(matrix) - j - 1][i]
