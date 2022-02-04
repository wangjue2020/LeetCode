# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, vin: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # write code here
        if len(postorder) == 0:
            return 
        if len(postorder) == 1:
            return TreeNode(postorder[0])
        if len(postorder) == 2:
            cur = TreeNode(postorder[1])
            if postorder == vin:
                cur.left = TreeNode(postorder[0])
            else:
                cur.right = TreeNode(postorder[0])
            return cur
        root = TreeNode(postorder[-1])
        ind = 0
        for i in range(len(vin)):
            if vin[i] == postorder[-1]:
                ind = i
                break 
        lvin = vin[:ind]
        rvin = vin[ind+1:]
        lpo = postorder[:len(lvin)]
        rpo = postorder[len(lvin):-1]
        root.left = self.buildTree( lvin,lpo)
        root.right = self.buildTree( rvin,rpo)
        return root