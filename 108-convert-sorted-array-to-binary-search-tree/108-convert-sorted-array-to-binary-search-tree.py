# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.buildBST(nums)
    def buildBST(self, nums):
        if len(nums) == 1:
            return TreeNode(nums[0])
        else:
            mid = len(nums) // 2
            left = self.buildBST(nums[:mid])
            right = None
            if mid+1 < len(nums):
                right = self.buildBST(nums[mid+1:])
            root = TreeNode(nums[mid], left, right)
            return root
            