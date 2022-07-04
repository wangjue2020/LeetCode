class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()
        r,c = len(matrix), len(matrix[0])
        arow = [0 for i in range(c)]
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        # change row
        for i in row:
            matrix[i] = arow[:]
        
        for i in range(r):
            for j in col:
                matrix[i][j] = 0
                    