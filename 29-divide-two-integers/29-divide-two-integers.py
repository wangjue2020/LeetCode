class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        pos = True
        MAX_INT = 2147483647
        MIN_INT = -2147483648 
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        if divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend
        if dividend < 0:
            pos = False
            dividend = -dividend
        if divisor < 0:
            pos = not pos
            divisor = - divisor
        ans = 0
        power = []
        res = []
        i = 1
        while i*divisor <= dividend:
            power.append(i)
            res.append(i*divisor)
            i=i*2
        
        for i in range(len(res)-1,-1, -1):
            if dividend > res[i]:
                ans += power[i]
                dividend -= res[i]
            elif dividend == res[i]:
                ans += power[i]
                break
        return ans if pos else -ans