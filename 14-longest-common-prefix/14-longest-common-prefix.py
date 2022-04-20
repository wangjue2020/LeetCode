class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        i = 0
        while True:
            cur = ''
            b = False
            for s in strs:
                if i >= len(s):
                    b=True
                    break
                if cur == '':
                    cur = s[i]
                else:
                    if s[i] != cur:
                        b=True
                        break
            if b:
                break
            else:
                ans +=cur
                i+= 1
        return ans
            