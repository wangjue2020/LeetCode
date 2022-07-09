# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.paths = 0
        self.dfs(root, '')
        # ans = 0
        # for i in self.paths:
        #     ans += int(i)
        return self.paths
    def dfs(self, root, curPath):
        if root == None:
            return
        if root.left == None and root.right == None:
            self.paths+=int(curPath+str(root.val))
        else:
            self.dfs(root.left, curPath+str(root.val))
            self.dfs(root.right, curPath+str(root.val))
            