class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.list = {}
        self.first = ListNode(-1, None, None, None)
        self.last = ListNode(-1, None, self.first, None)
        self.first.next = self.last
        self.size = 0
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_node(self, node):
        node.prev = self.last.prev
        self.last.prev.next = node
        node.next = self.last 
        self.last.prev = node

    def _move_to_end(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _remove_top(self):
        top = self.first.next
        del self.list[top.key]
        self.first.next = self.first.next.next
        self.first.next.prev = top.prev

    def get(self, key: int) -> int:
        node = self.list.get(key)
        if node is None:
            return -1
        self._move_to_end(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.list.get(key)
        if node != None:
            node.val = value
            self._move_to_end(node)
            self.list[key] = node
        else:
            node = ListNode(key, value, self.last, None)
            self._add_node(node)
            self.size+=1
            self.list[key] = node
            if self.size>self.capacity:
                self._remove_top()
                self.size-=1
    def __str__(self):
        s = ""
        tmp = self.first
        while tmp != None:
            s += f"[{tmp.key}={tmp.val}] -->"
            tmp = tmp.next
        ss = ""
        tmp = self.last
        while tmp!= None:
            ss = f"[{tmp.key}={tmp.val}] -->" + ss 
            tmp = tmp.prev 
        s += '\n'
        s += ss
        return s
            



class ListNode:
    def __init__(self, key, val, prev, next):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
