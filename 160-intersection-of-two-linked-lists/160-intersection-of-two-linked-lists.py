# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n1 = headA
        n2 = headB
        while n1 != n2:
            n1 = n1.next if n1 != None else headB
            n2 = n2.next if n2 != None else headA
        return n1
        