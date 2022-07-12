class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []
        if nums == []:
            cur = str(lower)
            if upper > lower:
                cur += '->'+str(upper)
            return [cur]
        target = lower
        cur_miss = ''
        i = 0
        while target < upper and i < len(nums):
            if nums[i] == target:
                target += 1
                
            else:
                start = target
                end = nums[i]-1
                if start == end:
                    ans.append(str(start))
                else:
                    ans.append(str(start)+'->'+str(end))
                target = end+2
            i+= 1
        if nums[-1]< upper:
            if nums[-1]+1 == upper:
                ans.append(str(upper))
            else:
                ans.append(str(nums[-1]+1)+'->'+str(upper))
        return ans