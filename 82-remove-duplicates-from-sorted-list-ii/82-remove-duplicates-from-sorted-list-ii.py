# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = None
        if head == None:
            return
        last = None
        ptr = head
        dup = False
        while ptr != None:
            if p != None and ptr.val == p.val:
                p.next = ptr.next
                ptr = ptr.next 
                dup = True
            else:
                if dup:
                    if last != None:
                        last.next = ptr
                    else:
                        head = ptr
                    dup = False
                else:
                    last = p
                p = ptr 
                ptr = ptr.next 
        if last != None and dup:
            last.next = ptr
        return head if not dup or last != None else None