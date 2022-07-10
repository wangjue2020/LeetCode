class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        neg = 0
        pos = 0
        for i in range(len(nums)):
            if i == 0:
                neg = min(neg, nums[i])
                pos = max(pos, nums[i])
            else:
                if nums[i] == 0:
                    ans = max(ans, pos)
                    neg = 0
                    pos = 0
                else:
                    a = nums[i]
                    b = nums[i] * neg
                    c = nums[i] * pos
                    neg = min(a, min(b,c))
                    pos = max(a, max(b,c))
                    ans = max(pos, ans)
        return ans
                    
        