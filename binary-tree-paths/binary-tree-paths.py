# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans=[]
        self.dfs(root, '')
        return self.ans
    def dfs(self, root, curPath):
        if root == None:
            return
        if root.left == None and root.right == None:
            if curPath == '':
                self.ans.append(curPath+str(root.val))
            else:
                self.ans.append(curPath+'->'+str(root.val))
        else:
            if curPath != '':
                curPath += '->'
            self.dfs(root.left, curPath+str(root.val))
            self.dfs(root.right, curPath+str(root.val))
        