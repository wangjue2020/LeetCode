class Solution:
    def romanToInt(self, s: str) -> int:
        l = []
        d = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
        i = 0
        while i < len(s):
            while i < len(s) and (l==[] or d[s[i]] > l[-1]):
                l.append(d[s[i]])
                i+=1
            plus = 1
            while l != []:
                ans += plus*l.pop()
                plus = -1* plus
        return ans
                    