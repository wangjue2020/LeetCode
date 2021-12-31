# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -100000;
        self.postorder(root)
        return self.max_sum
    def postorder(self, root):
        if root == None:
            return ;
        if root.left == None and root.right == None:
            cur_sum = root.val
            self.max_sum = cur_sum if cur_sum >= self.max_sum else self.max_sum
            return cur_sum
        else:
            
            
            cur_sum_l = root.val
            if root.left !=  None:
                left = self.postorder(root.left)
                if cur_sum_l > 0 and left < 0:
                    cur_sum_l = cur_sum_l
                elif left >=0 and cur_sum_l + left < 0:
                    self.max_sum = left if left > self.max_sum else self.max_sum
                else:
                    cur_sum_l += left
                
            cur_sum_r = root.val
            if root.right != None:
                right = self.postorder(root.right)
                if cur_sum_r > 0 and right < 0:
                    cur_sum_r = cur_sum_r
                elif right >=0 and cur_sum_r + right < 0:
                    self.max_sum = right if right > self.max_sum else self.max_sum
                else:
                    cur_sum_r+= right
            self.max_sum = cur_sum_l if cur_sum_l > self.max_sum else self.max_sum
            self.max_sum = cur_sum_r if cur_sum_r > self.max_sum else self.max_sum
            sum_l_r = cur_sum_l+cur_sum_r - root.val
            self.max_sum = sum_l_r if sum_l_r > self.max_sum else self.max_sum
            return max(cur_sum_r,cur_sum_l)
            
            