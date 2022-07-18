class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        changed = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                cnt = 0
                # 1
                if r-1 >= 0 and c-1>=0 and board[r-1][c-1]==1:
                    cnt += 1
                if r-1>=0 and board[r-1][c] ==1:
                    cnt +=1
                if r-1>=0 and c+1 <len(board[0]) and board[r-1][c+1]==1:
                    cnt += 1
                if c-1 >=0 and board[r][c-1] == 1:
                    cnt += 1
                if c+1 < len(board[0]) and board[r][c+1] == 1:
                    cnt += 1
                if r+1 <len(board) and c-1>=0 and board[r+1][c-1] == 1:
                    cnt += 1
                if r+1 < len(board) and board[r+1][c]==1:
                    cnt+=1
                if r+1 < len(board) and c+1 < len(board[0]) and board[r+1][c+1]==1:
                    cnt+=1
                if board[r][c] ==1:
                    if cnt < 2 or cnt > 3:
                        changed.append((r,c))
                if board[r][c] == 0:
                    if cnt ==3:
                        changed.append((r,c))
        for e in changed:
            board[e[0]][e[1]] = abs(board[e[0]][e[1]]-1)