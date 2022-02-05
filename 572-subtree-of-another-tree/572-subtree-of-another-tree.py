# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, pRoot1: Optional[TreeNode], pRoot2: Optional[TreeNode]) -> bool:
        if pRoot1 == None and pRoot2==None:
            return False
        if pRoot1 == None or pRoot2 == None:
            return False
        l = [pRoot1]
        while len(l) > 0:
            cur = l.pop()
            if cur.val == pRoot2.val:
                if self.isSameTree(cur, pRoot2):
                    return True
            if cur.right != None:
                l.append(cur.right)
            if cur.left != None:
                l.append(cur.left)
        return False
    def isSameTree(self, t1, t2):
        if t1 == None and t2 == None:
            return True
        if t1 == None or t2 == None:
            return False
        if t1.val == t2.val:
            return self.isSameTree(t1.left, t2.left) and self.isSameTree(t1.right, t2.right)
        return False