class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            cur = nums[i]
            l = i+1
            r = len(nums)-1
            while l < r:
                addition = cur + nums[l] + nums[r]
                if addition < 0:
                    l+=1
                elif addition == 0:
                    if [cur, nums[l], nums[r]] not in ans:
                        ans.append([cur, nums[l], nums[r]])
                    l+=1
                    r-=1
                else:
                    r-=1
        return ans
            