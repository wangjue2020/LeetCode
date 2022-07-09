class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.list = {}
        self.first = ListNode(-1)
        self.last = ListNode(-1,prev = self.first)
        self.first.next = self.last
        self.size = 0
    
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_node(self,node):
        node.prev = self.last.prev
        self.last.prev.next = node
        node.next = self.last
        self.last.prev = node
        
    def get(self, key: int) -> int:
        cur = self.list.get(key)
        if cur is None:
            return -1
        else:
            self._remove_node(cur)
            self._add_node(cur)
            return cur.val

    def put(self, key: int, value: int) -> None:
        cur = self.list.get(key)
        if cur != None:
            cur.val = value
            self._remove_node(cur)
            self._add_node(cur)
        else:
            cur = ListNode(key, val=value)
            self._add_node(cur)
            self.list[key] = cur
            self.size += 1
            if self.capacity< self.size:
                self.size -=1
                del self.list[self.first.next.key]
                self._remove_node(self.first.next)
        
class ListNode:
    def __init__(self, key, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)