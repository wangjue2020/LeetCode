# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = ListNode(-1,head)
        a = head 
        b = head
        head = p
        for i in range(n):
            if b == None:
                return None
            b = b.next
        while b!= None:
            p = a
            a = a.next 
            b = b.next 
        if p.next != None:
            p.next = p.next.next
        return head.next