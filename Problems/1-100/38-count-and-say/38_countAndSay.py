import unittest
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        res = self.countAndSay(n-1)
        cur = res[0]
        count = 1
        ans = ''
        for i in range(1,len(res)):
            if res[i] == cur:
                count+=1
            else:
                ans += str(count)+cur
                count = 1
                cur = res[i]
        ans += str(count)+cur
        return ans

class TestSolution(unittest.TestCase):
    def test_countAndSay(self):
        s = Solution()
        self.assertEqual(s.countAndSay(1),'1')
        self.assertEqual(s.countAndSay(2),'11')
        self.assertEqual(s.countAndSay(3),'21')
        self.assertEqual(s.countAndSay(4),'1211')
    
if __name__ == '__main__':
    unittest.main()