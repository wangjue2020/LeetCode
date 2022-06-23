class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            cur = target - nums[i] 
            if cur in visited:
                return [i, visited[cur]]
            else:
                visited[nums[i]] = i
        