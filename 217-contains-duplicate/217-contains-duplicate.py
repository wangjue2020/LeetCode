class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        cur = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == cur:
                return True
            else:
                cur = nums[i]
        return False