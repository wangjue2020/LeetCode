class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = 0
        cur = 0
        for i in range(len(nums)):
            if i == 0:
                ans = nums[i]
                cur = nums[i]
            else:
                if nums[i] >= 0:
                    cur = max(nums[i], nums[i] + cur)
                else:
                    ans = max(cur, ans)
                    cur = max(nums[i], nums[i]+cur)
        return max(ans, cur)