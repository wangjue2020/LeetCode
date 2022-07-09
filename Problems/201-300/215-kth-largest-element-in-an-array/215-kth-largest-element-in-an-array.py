class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ll = ListNode(-1, None)
        last = ll
        capacity = 0
        for i in range(len(nums)):
            ll = self.insert(k, ll, nums[i], capacity)
            if capacity + 1 > k:
                ll.next = ll.next.next
            else:
                capacity += 1
        return ll.next.val
    
    def insert(self, k, ll, val, capacity ):
        node = ListNode(val, None)
        tmp = ll.next
        prev = ll
        while tmp != None:
            if tmp.val < val:
                prev = tmp
                tmp = tmp.next
            else:
                break
        prev.next = node
        node.next = tmp
        return ll

class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next