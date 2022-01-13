# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
             return head
        p = None
        cur = head
        child = cur.next
        while child != None:
            cur.next = p
            p = cur
            cur = child
            child = cur.next
        cur.next = p
        return cur