class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        cur = nums[0]
        cnt = 1
        for i in nums[1:]:
            if i == cur:
                cnt += 1
            else:
                if cnt == 1:
                    return cur
                else:
                    cnt = 1
                    cur = i
        return cur