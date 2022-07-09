class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # write code here
        r= len(matrix)
        if r== 0:
            return
        c = len(matrix[0])
        self.ans = []
        self.print1(matrix, 0, r-1, 0, c-1)
        return self.ans
    def print1(self, matrix, sr, er, sc, ec):
        if er < 0 or ec < 0:
            return
        r = er-sr+1
        if r == 0:
            return
        c = ec-sc +1
        if c == 0:
            return
        i = sr
        j = sc
        if r > 1 and c > 1:
            total = 2*c + 2*(r-2)
        else:
            total = r if c == 1 else c
        for x in range(total):
            self.ans.append(matrix[i][j])
            if i==sr and j < ec:
                j+=1
            elif i < er and j == ec:
                i+=1
            elif i == er and j >sc:
                j-=1
            elif i>sr and j==sc:
                i-=1
        self.print1(matrix,sr+1,er-1,sc+1,ec-1)