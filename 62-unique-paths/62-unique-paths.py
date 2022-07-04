class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        row = [0 for i in range(n)]
        maps = [row for i in range(m)]
        # initialize
        for i in range(n):
            maps[0][i] = 1
        for i in range(m):
            maps[i][0] = 1
                
        for i in range(1, m):
            for j in range(1,n):
                maps[i][j] = maps[i-1][j] + maps[i][j-1]
        
        return maps[-1][-1]