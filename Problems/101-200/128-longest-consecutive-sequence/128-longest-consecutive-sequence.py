class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums = set(nums)
        for i in nums:
            if i-1 not in nums:
                cur_ans = 1
                cur_num = i
                
                while cur_num + 1 in nums:
                    cur_ans += 1
                    cur_num +=1
                
                ans = max(ans, cur_ans)
        return ans