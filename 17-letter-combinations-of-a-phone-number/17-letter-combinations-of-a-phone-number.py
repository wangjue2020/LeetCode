class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        ans = []
        d = [[],[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],\
            ['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        if len(digits) == 1:
            return d[int(digits)]
        for i in range(len(digits)):
            cur = int(digits[i])
            cur_char = d[cur]
            if ans == []:
                ans = cur_char[:]
                continue
            l = len(ans)
            for j in range(l):
                pre = ans.pop()
                added = [pre+letter for letter in cur_char]
                ans = added+ans
        return ans
                
            