class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
            
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals, key=lambda x : x[0])
        print(intervals)
        l = intervals[0][0]
        r = intervals[0][1]
        ans = []
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] >= l and cur[0] <= r:
                r = max(r, cur[1])
            elif cur[0] >r:
                ans.append([l,r])
                l = cur[0]
                r = cur[1]
        ans.append([l,r])
        return ans