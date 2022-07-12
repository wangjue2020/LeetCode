class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ans = 0
        
        for i in range(1, len(nums)):
            if nums[i] > nums[ans]:
                ans = i
        return ans