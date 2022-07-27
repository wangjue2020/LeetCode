class Solution:
    def isHappy(self, n: int) -> bool:
        self.l = set()
        self.l.add(n)
        return self.helper(n)
    def helper(self, n):
        if n < 10 and n==1:
            return True
        else:
            # print(n)
            prev = n
            nex = 0
            while n> 0:
                nex += (n%10)**2
                n = n // 10
            # print(nex)
            if nex in self.l:
                return False
            self.l.add(nex)
            return self.helper(nex)