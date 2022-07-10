class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return self.recursion(list(s))
    def isPalindrom(self, s):
        if len(s) <= 1:
            return True
        if len(s) == 2:
            return s[0]==s[-1]
        else:
            if s[0] == s[-1]:
                return self.isPalindrom(s[1:-1])
            else:
                return False
    def recursion(self,l):
        if len(l)<=1:
            return [l]
        else:
            ans = []
            for i in range(len(l)):
                prefix = ''.join(l[:i+1])
                if self.isPalindrom(prefix):
                    for e in self.recursion(l[i+1:]):
                        ans.append([prefix]+e)
            return ans