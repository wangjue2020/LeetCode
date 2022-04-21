class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        l = ['{', '(', '[']
        r = ['}',']',')']
        d = {'{':0, '(':1, '[':2,'}':0,']':2,')':1}
        stack = []
        for i in range(len(s)):
            cur = s[i]
            if cur in l:
                stack.append(cur)
            else:
                if stack==[]:
                    return False
                last = stack.pop()
                if d[cur] == d[last]:
                    continue
                else:
                    return False
        return stack == []