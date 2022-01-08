class Solution:
    def findMin(self, nums: List[int]) -> int:
        mi= self.findMinimum(nums, 0, len(nums)-1)
        return  mi
    def findMinimum(self, nums, s, e):
        if s== e:
            return nums[s]
        else:
            mid = (e-s) // 2 + s
            left = self.findMinimum(nums,s,mid)
            right = self.findMinimum(nums, mid+1,e)
            if left < right:
                return left
            else:
                return right