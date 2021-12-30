# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q
        self.ancestor = None
        self.dfs(root)
        return self.ancestor
        
    def dfs(self, root):
        if root== None:
            return 0
        cur = 0
        if root == self.p or  root == self.q:
            cur = 1   
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if left + right + cur>= 2:
            if self.ancestor == None:
                self.ancestor = root
                return 0
        else:
            return max(left, max(cur,right))