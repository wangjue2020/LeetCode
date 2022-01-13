# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rev1 = self.reverse(l1)
        rev2 = self.reverse(l2)
        
        addon = 0
        ans = rev1
        prev = None
        while rev1 != None:
            if addon == 0 and rev2 == None:
                break
            if addon != 0:
                rev1.val += addon
            if rev2 != None:
                rev1.val += rev2.val
                rev2 = rev2.next
            addon = rev1.val // 10
            rev1.val = rev1.val %10
            prev = rev1
            rev1 = rev1.next
            if rev1 == None and rev2 != None:
                prev.next = rev2
                rev1 = rev2
                rev2 = None
        if addon == 1:
            prev.next = ListNode(1)
        return self.reverse(ans)
    def reverse(self, l):
        p = None
        cur = l
        child = cur.next
        while child != None:
            cur.next = p
            p = cur
            cur = child
            child = child.next
        cur.next = p
        return cur
        