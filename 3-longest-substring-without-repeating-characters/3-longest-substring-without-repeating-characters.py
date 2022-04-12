class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        second = -1
        sub = ''
        ans=0
        for i in range(len(s)):
            if s[i] not in sub:
                second = i
                sub += s[i]
                ans = max(ans, len(sub))
            else:

                ans = max(ans, len(sub))
                ind = sub.find(s[i])
                # first = i-len(sub)+ind
                sub = sub[ind+1:]+s[i]
        return ans  