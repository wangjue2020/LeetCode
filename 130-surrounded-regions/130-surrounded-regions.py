class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.visited=set()
        border = []
        self.M,self.N = len(board), len(board[0])
        self.o = []
        for i in range(self.M):
            if board[i][0] == 'O':
                border.append((i,0))
            if board[i][-1]=='O':
                border.append((i,self.N-1))
        for i in range(self.N):
            if board[0][i] == 'O':
                border.append((0,i))
            if board[-1][i] == 'O':
                border.append((self.M-1,i))
        
        for cur in border:
            
            self.dfs(board, cur)
        
        for i in range(self.M):
            for j in range(self.N):
                if board[i][j] =='O' and (i,j) not in self.o:
                    board[i][j] = 'X'
            
    def dfs(self, board,root):
        l=[root]
        while l != []:
            cur = l.pop()
            cur_r, cur_c = cur[0], cur[1]
            self.o.append((cur_r, cur_c))
            # up, down, left, right
            if cur_r -1 >= 0 and board[cur_r-1][cur_c] == 'O' and (cur_r-1, cur_c) not in self.visited:
                l.append((cur_r-1, cur_c))
                self.visited.add((cur_r-1, cur_c))
            if cur_r+1<self.M and board[cur_r+1][cur_c] == 'O' and (cur_r+1, cur_c) not in self.visited:
                l.append((cur_r+1, cur_c))
                self.visited.add((cur_r+1, cur_c))
            if cur_c-1 >= 0 and board[cur_r][cur_c-1]=='O' and (cur_r, cur_c-1) not in self.visited:
                l.append((cur_r, cur_c-1))
                self.visited.add((cur_r, cur_c-1))
            if cur_c+1<self.N and board[cur_r][cur_c+1]=='O' and (cur_r, cur_c+1) not in self.visited:
                l.append((cur_r, cur_c+1))
                self.visited.add((cur_r, cur_c+1))
                
        