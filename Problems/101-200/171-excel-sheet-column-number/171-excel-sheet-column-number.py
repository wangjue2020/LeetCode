class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        deg = 0
        for i in range(len(columnTitle)-1, -1,-1):
            ans += (26**deg) * (1+ord(columnTitle[i])-ord('A'))
            deg+=1
        return ans