class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        res = self.countAndSay(n-1)
        cur = res[0]
        count = 1
        ans = ''
        for i in range(1,len(res)):
            if res[i] == cur:
                count+=1
            else:
                ans += str(count)+cur
                count = 1
                cur = res[i]
                
        ans += str(count)+cur
        return ans