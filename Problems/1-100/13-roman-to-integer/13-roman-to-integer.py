class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}
        l = []
        ans = 0
        for i in range(len(s)):
            cur = dic[s[i]]
            if l==[]:
                l.append(cur)
            else:

                if cur < l[-1]:
                    ans += l.pop()
                    l.append(cur)
                elif cur == l[-1]:
                    l.append(cur)
                else:
                    ans += cur
                    while l != [] and cur >l[-1]:
                        ans -= l.pop()
        if l != []:
            ans += sum(l)
        return ans
                
            