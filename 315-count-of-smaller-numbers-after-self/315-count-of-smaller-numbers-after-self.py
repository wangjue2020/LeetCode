class Solution:
    def countSmaller(self, nums):
        sort = sorted(nums)
        mid = (sort[-1]+sort[0])//2
        reversed_num = self.reverse(nums)
        nums = []
        bst = self.buildbst(sort)
        for cur in reversed_num:
            count = 0
            tmp = bst
            while True:
                if tmp.val < cur:
                    count += tmp.freq+tmp.num_left
                    if tmp.right == None:
                        tmp.right = BSTNode(cur)
                        break
                    tmp = tmp.right
                elif tmp.val > cur:
                    if tmp.left == None:
                        tmp.left = BSTNode(cur)
                        tmp.num_left+=1
                        break
                    tmp.num_left+=1
                    tmp = tmp.left
                else:
                    tmp.freq+=1
                    count += tmp.num_left
                    break
            nums.append(count)
        return self.reverse(nums)
                        
    def reverse(self, nums):
        if len(nums) == 1:
            return nums
        else:
            mid = len(nums)//2
            left = self.reverse(nums[:mid])
            right = self.reverse(nums[mid:])
            return right+left
    
    def buildbst(self, nums):
        if nums==[]:
            return None
        elif len(nums) == 1:
            return BSTNode(nums[0])
        else:
            mid = len(nums)//2
            root = BSTNode(nums[mid])
            root.left = self.buildbst(nums[:mid])
            if mid+1 < len(nums):
                root.right = self.buildbst(nums[mid+1:])
            return root
    
        
    
class BSTNode:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None
        self.freq=0
        self.num_left=0
