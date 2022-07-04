class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l, r = 2, x//2
        while l <= r:
            mid = (r-l)//2+l
            res = mid * mid 
            if res == x:
                return mid
            elif res < x:
                l = mid+1
            else:
                r = mid-1
        return r