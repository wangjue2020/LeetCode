# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        else:
            min = float('-inf')
            max = float('inf')
            left = self.isvalid(root.left, min, root.val)
            right = self.isvalid(root.right, root.val, max)
            return left and right
    def isvalid(self, root, min,max):
        if root == None:
            return True
        if root.val > min and root.val < max:
            left =self.isvalid(root.left, min, root.val)
            right = self.isvalid(root.right, root.val, max)
            return left and right
        else:
            return False