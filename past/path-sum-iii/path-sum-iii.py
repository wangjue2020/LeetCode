# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans =0
        self.root = root
        self.targetSum = targetSum
        self.dfs(self.root, [])
        return self.ans
    def dfs(self, root, curPaths):
        if root == None:
            return 
        curPaths=[x+root.val for x in curPaths]
        count = curPaths.count(self.targetSum)
        self.ans += count
        if root.val == self.targetSum:
            self.ans += 1
        curPaths.append(root.val)   
        self.dfs(root.left, curPaths[:])
        self.dfs(root.right, curPaths[:])
