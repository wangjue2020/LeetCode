# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, pre: List[int], vin: List[int]) -> Optional[TreeNode]:
                # write code here
        if len(pre) == 0:
            return 
        if len(pre) == 1:
            return TreeNode(pre[0])
        if len(pre) == 2:
            cur = TreeNode(pre[0])
            if pre == vin:
                cur.right = TreeNode(pre[1])
            else:
                cur.left = TreeNode(pre[1])
            return cur
        root = TreeNode(pre[0])
        ind = 0
        for i in range(len(vin)):
            if vin[i] == pre[0]:
                ind = i
                break 
        lvin = vin[:ind]
        rvin = vin[ind+1:]
        lpre = pre[1:1+len(lvin)]
        rpre = pre[1+len(lvin):]
        root.left = self.buildTree(lpre, lvin)
        root.right = self.buildTree(rpre, rvin)
        return root