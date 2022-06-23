class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        ans = 0
        cur = 0
        while r < len(nums):
            if r == 0:
                cur = nums[r]
                ans = cur
            else:
                curn = nums[r]
                if cur < 0:
                    if cur + curn < cur:
                        ans = max(cur, ans)
                        cur = curn
                    else:
                        cur = curn
                else:
                    if cur + curn < cur and cur + curn >= 0:
                        ans = max(cur, ans)
                        cur = curn + cur
                    elif cur + curn < 0:
                        ans = max(cur, ans)
                        cur = curn
                    elif cur + curn > cur:
                        cur = curn + cur
            r += 1
        return ans if ans > cur else cur