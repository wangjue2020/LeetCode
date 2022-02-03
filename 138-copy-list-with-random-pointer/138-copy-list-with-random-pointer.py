"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}
        ans = None
        tmp = ans
        while head != None:
            if ans == None:
                ans = Node(head.val)
                tmp = ans
                d[head] = tmp
            if head.next != None:
                if head.next not in d:
                    n = Node(head.next.val)
                    d[head.next] = n
                tmp.next = d[head.next]
            if head.random != None:
                if head.random not in d:
                    r = Node(head.random.val)
                    d[head.random] = r
                tmp.random = d[head.random]
            head = head.next
            tmp = tmp.next
        return ans