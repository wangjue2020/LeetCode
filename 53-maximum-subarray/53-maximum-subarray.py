class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ans = nums[0]
        cur = ans
        for i in range(1, len(nums)):
            if nums[i] >= 0:
                cur = max(nums[i], cur+nums[i],)
            else:
                ans = max(ans, cur)
                cur = max(nums[i], cur + nums[i])
        ans = max(ans, cur)
        return ans
            
            