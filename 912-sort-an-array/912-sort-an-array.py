class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        else:
            mid = len(nums)//2
            left = self.sortArray(nums[:mid])
            right = self.sortArray(nums[mid:])
            return self.combine(left, right)
    def combine(self, left, right):
        l = 0
        r = 0
        ans = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                ans.append(left[l])
                l+=1
            elif left[l] == right [r]:
                ans.append(left[l])
                ans.append(right[r])
                l+=1
                r+=1
            else:
                ans.append(right[r])
                r+=1
        if l<len(left):
            ans += left[l:]
        if r<len(right):
            ans += right[r:]
        return ans