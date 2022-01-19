# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)
        else:
            ptr = root
            p = None
            while ptr!= None:
                if ptr.val > val:
                    p = ptr
                    ptr = ptr.left
                else:
                    p = ptr
                    ptr = ptr.right
            if p.val > val:
                p.left = TreeNode(val)
            else:
                p.right = TreeNode(val)
            return root