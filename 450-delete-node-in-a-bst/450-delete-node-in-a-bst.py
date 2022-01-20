# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return root
        
        p = TreeNode()
        if p.val >= root.val:
            p.left = root
            flag = True
            
        else:
            p.right = root
            flag = False
        
        ptr = root
        root = p
        while ptr != None:
            if ptr.val > key:
                p = ptr
                ptr = ptr.left
            elif ptr.val < key:
                p = ptr
                ptr = ptr.right
            else:
                origin = ptr
                if ptr.left == None and ptr.right == None:
                    ptr = None
                elif ptr.left == None:
                    ptr = ptr.right
                elif ptr.right == None:
                    ptr = ptr.left
                else:
                    backup = ptr.left
                    head = ptr.right
                    pp = p
                    while head != None and head.left != None:
                        head = head.left
                    head.left = backup
                    ptr = ptr.right
                if p.val >= origin.val:
                    p.left = ptr
                else:
                    p.right = ptr
        return root.left if flag else root.right