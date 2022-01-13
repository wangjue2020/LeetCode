# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head == None:
        #     return head
        ans = ListNode(-1, head)
        p = ans
        tmp = head
        while tmp != None and tmp.next != None:
            backup = tmp.next.next
            p.next = tmp.next
            tmp.next.next = tmp
            tmp.next = backup
            p = tmp
            tmp = tmp.next
        return ans.next