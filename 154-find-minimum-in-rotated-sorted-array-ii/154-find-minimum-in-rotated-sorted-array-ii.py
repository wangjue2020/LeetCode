class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.findMinimum(nums, 0, len(nums)-1)
    def findMinimum(self, nums, s,e):
        if s == e:
            return nums[s]
        else:
            mid = (e-s)//2+s
            l = mid
            while l-1 >= s and nums[l-1] == nums[l]:
                l = l-1
            left = self.findMinimum(nums, s, l)
            r = mid+1
            while r+1 <= e and nums[r+1] == nums[r]:
                r = r+1
            right = self.findMinimum(nums, r, e)
            if left <= right:
                return left
            else:
                return right