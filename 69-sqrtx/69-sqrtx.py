class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return x
        if x == 16:
            return 4
        elif x > 16:
            prev = 0
            for i in range(x//4+1):
                if i*i > x:
                    return i-1
                if i*i == x:
                    return i
            return x//4
        else:
            for i in range(x//4, x//2+1):
                if i*i > x:
                    return i-1
                if i*i == x:
                    return i
            return x//2     