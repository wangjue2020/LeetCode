class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        ans = 0
        dic = {}
        cur = 0
        while right < len(s):
            if right == 0:
                cur +=1
                dic[s[right]] = right
                right+= 1
            else:
                if s[right] in dic and dic[s[right]] >= left:
                    ans = max(ans, cur)
                    left = dic[s[right]] + 1
                    cur = right-left + 1
                    dic[s[right]] = right
                    right += 1
                    
                else:
                    cur +=1
                    dic[s[right]] = right
                    right+= 1
        return ans if cur <= ans else cur
        
        