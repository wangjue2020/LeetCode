# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.ans = float('inf')
        self.traversal(root)
        return self.ans
    def traversal(self, root):
        if root == None:
            return 
        if root.left == None and root.right == None:
            return [root.val, root.val]
        else:
            left = self.traversal(root.left)
            right = self.traversal(root.right)
            cur_min = root.val
            cur_max = root.val
            if left != None:
                minl,maxl = left[0],left[1]
                self.ans = min(abs(root.val- maxl), self.ans)
                cur_min = minl
            if right != None:
                minr, maxr = right[0], right[1]
                self.ans = min(abs(root.val-minr), self.ans)
                cur_max = maxr
            return [cur_min, cur_max]
                
            