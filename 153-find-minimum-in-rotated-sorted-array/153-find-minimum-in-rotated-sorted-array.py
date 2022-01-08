class Solution:
    def findMin(self, nums: List[int]) -> int:
        mi,ind = self.findMinimum(nums, 0, len(nums)-1)
        return  mi
    def findMinimum(self, nums, s, e):
        if s== e:
            return nums[s], s
        else:
            mid = (e-s) // 2 + s
            left,l_ind = self.findMinimum(nums,s,mid)
            right,r_ind = self.findMinimum(nums, mid+1,e)
            if left < right:
                return left, l_ind
            else:
                return right, r_ind