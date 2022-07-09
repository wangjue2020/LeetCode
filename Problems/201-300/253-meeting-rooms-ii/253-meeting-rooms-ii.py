class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        used_rooms = 0
        
        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])
        L = len(intervals)
        
        s = 0
        e = 0
        
        while s < L:
            if start_times[s] >= end_times[e]:
                used_rooms -= 1
                e+=1
            used_rooms += 1
            s +=1
        return used_rooms