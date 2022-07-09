class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        left = {'(':0, '[':1, '{':2}
        right = {')':0, ']':1, '}':2}
        
        for i in range(len(s)):
            if s[i] in left:
                l.append(s[i])
            else:
                if l == []:
                    return False
                lst = l[-1]
                if left[lst] == right[s[i]]:
                    l.pop()
                else:
                    return False
        return l == []