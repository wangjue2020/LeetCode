import unittest
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
        count = 0
        while dividend >= divisor:
            dividend -= divisor
            count+= 1
        if not pos:
            count = -count
        return count
    
    def divide_v2(self, dividend:int, divisor:int)->int:
        pos = True
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

class testSolution(unittest.TestCase):
    def test_divide(self):
        s = Solution()
        self.assertEqual(s.divide(10,3),3)
        self.assertEqual(s.divide(-10,-3),3)
        self.assertEqual(s.divide(-10,3),-3)
        self.assertEqual(s.divide(7,-3),-2)
    def test_divide(self):
        s = Solution()
        self.assertEqual(s.divide_v2(10,3),3)
        self.assertEqual(s.divide_v2(-10,-3),3)
        self.assertEqual(s.divide_v2(-10,3),-3)
        self.assertEqual(s.divide_v2(7,-3),-2)
        self.assertEqual(s.divide_v2(7,-13),0)
        self.assertEqual(s.divide_v2(2147483647,3),715827882)
if __name__ == '__main__':
    unittest.main()