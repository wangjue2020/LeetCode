class Solution:
    def search(self, nums: List[int], target: int) -> int:
       
        l = 0
        r = len(nums) -1 
        while r >= l:
            if r == l :
                return -1 if nums[l] != target else 0
            elif nums[l] < nums[r]:
                return self.regularsearch(nums, target, l, r)
            elif r-l == 1:
                if nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r
                else:
                    return -1
            else:
                mid = (r+l) //2
                if (nums[mid] == target):
                    return mid
                else:
                    leftpart_r = mid-1
                    rightpart_l = mid + 1
                    #border on the left
                    if nums[l] > nums[leftpart_r]:
                        if target >= nums[l] or target <= nums[leftpart_r]:
                            r = leftpart_r
                            
                        else:
                            l = rightpart_l
                            return self.regularsearch(nums, target,l, r)
                    #border on the right
                    elif nums[rightpart_l] > nums[r]:
                        if target <= nums[r] or target >= nums[rightpart_l]:
                            l = rightpart_l

                        else:
                            r = leftpart_r
                            return self.regularsearch(nums,target, l, r)
                    else:
                        if target > nums[r]:
                            r = leftpart_r
                            return self.regularsearch(nums,target, l ,r)
                        else:
                            l = rightpart_l
                            return self.regularsearch(nums,target,l ,r)

                            
        return -1
    def regularsearch(self, nums, target, l, r):
        while r >= l:
            mid = (r+l) //2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid-1
            else:
                l = mid + 1
        return -1
                        
    
        