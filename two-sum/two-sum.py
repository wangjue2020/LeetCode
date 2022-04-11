class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in d:
                return [d[remain], i]
            else:
                d[nums[i]] = i