class Solution:
    def transpose(self, matrix):
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                tmp = matrix[i][j]
                matrix[i][j], matrix[j][i] = matrix[j][i], tmp
        return matrix
    def reversed(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix)//2):
                tmp = matrix[i][j]
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], tmp
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reversed(matrix)