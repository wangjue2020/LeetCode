# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        self.count = 0
        self.max = 0
        self.cur = None
        self.ans = []
        self.inorder(root)
        if self.count > self.max:
            self.ans = [self.cur]
            self.max = self.count
        elif self.count == self.max and self.count != 0:
            self.ans.append(self.cur)
        return self.ans
    def inorder (self, root):
        if root == None:
            return
        else:
            self.inorder(root.left)
            # print(root.val)
            if self.cur == None or self.cur != root.val:
                if self.count > self.max:
                    self.ans = [self.cur]
                    self.max = self.count
                    self.cur = root.val
                    self.count = 1
                elif self.count == self.max and self.count != 0:
                    self.ans.append(self.cur)
                    self.cur = root.val
                    self.count = 1
                else:
                    self.cur = root.val
                    self.count = 1
            else:
                self.count += 1
            self.inorder(root.right)