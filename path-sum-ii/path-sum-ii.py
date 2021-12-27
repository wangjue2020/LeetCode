# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        self.targetSum = targetSum
        self.dfs(root, [],0)
        return self.ans
    def dfs(self, root, curPath, curSum):
        if root == None:
            return 
        if root.left == None and root.right == None:
            if root.val + curSum == self.targetSum:
                curPath.append(root.val)
                self.ans.append(curPath)
        else:
            self.dfs(root.left, curPath+[root.val], root.val+curSum)
            self.dfs(root.right, curPath+[root.val], root.val+curSum)