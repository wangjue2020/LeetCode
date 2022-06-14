class Solution:
    def isValidSudoku(self, board) -> bool:
        
        return self.checkHV(board, 0) and self.checkHV(board,1) and self.check33box(board)

    def checkHV(self, board, mode):
        for i in range(9):
            if mode == 0:
                cur = board[i]
            else:
                cur = [board[j][i] for j in range(9)]
            if not self.checkduplicate(cur):
                    return False
        return True
    def check33box(self, board):
        for i in range(0,7,3):
            for j in range(0,7,3):
                cur = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
                if not self.checkduplicate(cur):
                    return False
        return True
    def checkduplicate(self, cur):
        s = " ".join(cur)
        s = s.replace(".", "")
        s = s.split()
        before = len(s)
        after = len(set(s))
        if before!=after:
            return False
        return True