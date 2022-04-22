class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1,-1]
        def search(nums, start, end, target):
            if start == end:
                if start < len(nums) and nums[start] == target:
                    return [start,start]
                else:
                    return [-1,-1]
            else:
                mid = int((end-start)/2+start)
                left = search(nums, start, mid, target)
                right = search(nums, mid+1, end, target)
                first = left[0] if left[0] != -1 else right[0]
                second = right[1] if right[1] != -1 else left[1]
                return [first, second]
        return search(nums, 0, len(nums)-1, target)