# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ptr = root
        if root == None:
            return root
        l = [root]
        while len(l) > 0:
            cur = l.pop()
            cur.left, cur.right = cur.right, cur.left
            if cur.right != None:
                l.append(cur.right)
            if cur.left != None:
                l.append(cur.left)
        return root