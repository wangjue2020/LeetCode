# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root))
    def dfs(self, root):
        if root == None:
            return 0,0
        if root.left == None and root.right == None:
            # print(root.val)
            # print([root.val,0])
            return [root.val, 0]
        else:
            left_sum,max_c_ccl = self.dfs(root.left)
            right_sum, max_c_ccr = self.dfs(root.right)
            max_c_cc = max(left_sum+right_sum, left_sum+max_c_ccr, right_sum+max_c_ccl, max_c_ccr+max_c_ccl)
            return [root.val+max_c_ccl+max_c_ccr, max_c_cc]