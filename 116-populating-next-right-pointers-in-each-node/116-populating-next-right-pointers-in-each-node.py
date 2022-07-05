"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root
        l = []
        tmp = root
        l= [root]
        while l != []:
            size = len(l)
            for i in range(size):
                cur = l.pop(0)
                if i<size-1:
                    cur.next = l[0]
                if cur.left is not None:
                    l.append(cur.left)
                if cur.right is not None:
                    l.append(cur.right)
        return root