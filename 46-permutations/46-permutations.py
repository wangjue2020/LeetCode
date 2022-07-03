class Solution:
    def addToAllList(self, ele, lists):
        return [[ele]+ i for i in lists]
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]
        if len(nums) == 2:
            return [nums, [nums[1], nums[0]]]
        else:
            ans = []
            for i in range(len(nums)):
                ans += self.addToAllList(nums[i], self.permute(nums[:i]+nums[i+1:]))
            return ans