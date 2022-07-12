class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k % len(nums) == 0:
            return
        k = k % len(nums)
        first = nums[-k:]
        for i in range(len(nums)-1,k-1,-1):
            nums[i] = nums[i-k]
        nums[:k] = first
        