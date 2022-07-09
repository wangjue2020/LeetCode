class Solution:
    def findWholeDigit(self, s, i):
        ans = ''
        while i < len(s) and s[i].isdigit():
            ans+=s[i]
            i+=1
        return ans, i-1
    def calculate(self, s: str) -> int:
        l = []
        i = 0
        s = s.replace(' ', '')
        cur = ''
        while i < len(s):
            cur = s[i]
            if s[i].isdigit():
                cur, i = self.findWholeDigit(s,i)
            if l == [] :
                l.append(cur)
                i+=1
            else:
                if cur in ["*", '/']:
                    last = float(l.pop())
                    next_d, next_i = self.findWholeDigit(s, i+1)
                    i = next_i+1
                    next = float(next_d)
                    new = last*next if cur=='*' else last//next
                    l.append(str(new))
                else:
                    l.append(cur)
                    i+=1
        ans = 0
        mode = 0
        for i in l:
            if mode == 0:
                ans += float(i)
                mode = -1
            elif mode == 1:
                ans -= float(i)
                mode = -1
            else:
                mode = 0 if i=='+' else 1

        return int(ans)


            