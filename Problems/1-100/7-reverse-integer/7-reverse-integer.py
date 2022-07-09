class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        origin = x
        if x < 0:
            x = -x
        while x > 0:
            last_digit = x % 10
            x = x //10
            if ans < (2**31 - last_digit -1)/10:
                ans = ans*10 + last_digit
            else:
                if origin < 0 and ans < (2**31 - last_digit)/10:
                    ans = ans * 10 + last_digit
                else:
                    return 0
                
        return ans if origin > 0 else -ans