class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        area = 0
        while l < r:
            width = r-l
            h = min(height[r], height[l])
            area = max(area, width*h)
            if h == height[l]:
                l+=1
            else:
                r-=1
        return area