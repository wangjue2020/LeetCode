class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s)-1
        while l<r:
            if not s[l].isalpha() and not s[l].isdigit():
                l+=1
                continue
            if not s[r].isalpha() and not s[r].isdigit():
                r-=1
                continue
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                return False
        return True