class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ind = 0
        ptr = 0
        pre = None
        while ptr < len(nums):
            if pre == None:
                pre = nums[ptr]
                ind += 1
                ptr += 1
            else:
                if nums[ptr] == pre:
                    ptr += 1
                else:
                    nums[ind] = nums[ptr]
                    pre = nums[ind]
                    ind += 1
                    ptr += 1
        return ind