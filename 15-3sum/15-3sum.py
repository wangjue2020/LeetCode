class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            first = nums[i]
            l = i+1
            r = len(nums) -1 
            if first > 0:
                break
            while l<r:
                second = nums[l]
                third = nums[r]
                if first + second + third == 0:
                    if [first, second, third] not in ans:
                        ans.append([first, second, third])
                    l+=1
                    r-=1
                elif first+second+third > 0:
                    r -=1
                else:
                    l+=1
        return ans