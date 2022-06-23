class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        ans = []
        l, r = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] > r:
                ans += [[l,r]]
                l, r = cur[0], cur[1]
            elif cur[0] <= r:
                r= max(r, cur[1])
                
        ans+=[[l,r]]
        return ans