class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        ele =[0 for i in range(length)]
        p = [ele[:] for i in range(length)]
        ans = ''
        #         initialization
        for i in range(length):
            p[i][i] = 1
            cur = s[i]
            if i < length-1:
                if s[i]==s[i+1]:
                    p[i][i+1] = 1 
                    cur = s[i:i+2]
            if len(cur) > len(ans):
                ans = cur
        for i in range(length-1, -1, -1):
            for j in range(i+2, length):
                p[i][j] = 1 if p[i+1][j-1] == 1 and s[i]==s[j] else 0
                if p[i][j] == 1:
                    ans = s[i:j+1] if len(s[i:j+1]) > len(ans) else ans
        return ans