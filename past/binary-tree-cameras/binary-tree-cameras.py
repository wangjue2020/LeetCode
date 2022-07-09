# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        final = self.dfs(root)
        if final == 2:
            self.ans += 1
        return self.ans
    def dfs(self, root):
#        -1 camera, 2 children of camera, 3 parent of camera 
        if root == None:
            return 3
        if root.left == None and root.right == None:
            return 2;
        else:
            left = self.dfs(root.left)
            right = self.dfs(root.right)
            if -1 in [left, right]:
                if left == -1:
                    if right == 2:
                        self.ans+=1
                        return -1
                    if right == 3:
                        return 3
                if right == -1:
                    if left == 2:
                        self.ans += 1
                        return -1
                    if right == 3:
                        return 3
                return 3
            elif 2 in [left, right]:
                self.ans += 1
                return -1
            elif left == 3 and right ==3:
                return 2;
                
                
                    