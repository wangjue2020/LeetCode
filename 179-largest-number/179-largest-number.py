class LargerNumKey(str):
    def __lt__(x,y):
        return x+y > y+x
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        nums.sort(key=LargerNumKey)
        ans = ''.join(nums)
        return '0' if ans[0] == '0' else ans
    
    
        