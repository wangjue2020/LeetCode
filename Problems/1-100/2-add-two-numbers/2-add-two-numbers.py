# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        add = 0
        p1 = l1
        p2 = l2
        prev = None
        while p1 != None and p2 != None:
            add = p1.val + p2.val + add
            p1.val = add % 10
            add = add // 10
            prev = p1
            p1 = p1.next
            p2 = p2.next
        if p2 != None:
            prev.next = p2
            p1 = p2
        if p1 != None:
            while p1 != None:
                add =p1.val + add
                p1.val = add % 10
                add = add // 10
                prev = p1
                p1 = p1.next
        if add == 1:
            prev.next = ListNode(1)
        return l1
        