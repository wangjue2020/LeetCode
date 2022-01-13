# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        addon = 0
        ans = l1
        prev1 = None
        prev2 = None
        while l1!= None:
            if addon == 0 and l2 == None:
                break
            if addon != 0:
                l1.val += addon
            if l2 != None:
                l1.val += l2.val
                l2 = l2.next
            addon = l1.val // 10
            l1.val = l1.val % 10
            prev1 = l1
            l1 = l1.next
            if l2 != None and l1==None:
                prev1.next = l2
                l1 = l2
                l2 = None
        if addon == 1:
            prev1.next = ListNode(1)
        return ans