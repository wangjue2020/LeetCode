# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.first = None
        self.second = None
        self.inorder(root)
        # print(self.first)
        # print(self.second)
        backup = self.first.val
        self.first.val = self.second.val
        self.second.val = backup
        return root
        
    def inorder(self, root):
        if root==None:
            return
        else:
            self.inorder(root.left)
            cur = root
            if self.prev != None and self.prev.val > cur.val:
                    if self.first == None:
                        self.first = self.prev
                    self.second = cur
            self.prev = cur
            self.inorder(root.right)