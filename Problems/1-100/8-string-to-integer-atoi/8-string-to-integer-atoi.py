class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        start = False
        f = False
        divid = 1
        positive = True
        max_int = 2**31-1
        min_int = -2**31
        for i in range(len(s)):
            cur = s[i]
            if not start and cur == ' ':
                continue
            if not start and cur in ['-', '+']:
                positive = False if cur == '-' else True
                start = True
                continue
            if cur == '.':
                f = True
                divid = 10
                break
            if cur.isdigit():
                start = True
                if ans < (max_int-int(cur)) / 10:
                    ans = ans * 10 + int(cur)
                else:
                    if not positive and ans < (2**31-int(cur)) / 10:
                        ans = ans * 10 + int(cur)
                    else:
                        return max_int if positive else min_int


            else:
                break
        return ans if positive else -ans