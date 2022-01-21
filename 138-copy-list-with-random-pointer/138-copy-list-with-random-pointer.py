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
        ans = Node(-1)
        ptr = ans
        ori = {}
        new = []
        ind = 0
        while head != None:
            if head not in ori:
                ptr.next = Node(head.val)
                ori[head] = ind
                new.append(ptr.next)
                ind+=1
            else:
                ptr.next = new[ori[head]]
            newnext = None
            if head.next != None:
                if head.next not in ori:
                    newnext = Node(head.next.val)
                    ori[head.next] = ind
                    new.append(newnext)
                    ind+=1
                else:
                    newnext = new[ori[head.next]]
            newrandom = None
            if head.random != None:
                if head.random not in ori:
                    newrandom = Node(head.random.val)
                    ori[head.random] = ind
                    new.append(newrandom)
                    ind+=1
                else:
                    newrandom = new[ori[head.random]]
            ptr.next.next = newnext
            ptr.next.random = newrandom
            ptr = ptr.next
            head= head.next
        return ans.next