class Solution:
    def canJump(self, nums: List[int]) -> bool:
        noZero = True
        for i in range(len(nums)-2,-1,-1):
            if noZero and nums[i] > 0 :
                continue
            elif nums[i] == 0 and noZero:
                noZero = False 
                steps = 2
                continue
            if not noZero:
                if nums[i] >= steps:
                    noZero = True
                else:
                    steps += 1
        return noZero
                
                