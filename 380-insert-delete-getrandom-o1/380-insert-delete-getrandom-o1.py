from random import choice
class RandomizedSet:

    def __init__(self):
        self.set = {}
        self.corpus = ListNode(-1, None)
        self.last = self.corpus
    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.set[val] = val
        node = ListNode(val, None)
        self.last.next = node
        self.last = node 
        return True
    def remove(self, val: int) -> bool:
        if val in self.set:
            del self.set[val]
            return True
        return False
        
    def getRandom(self) -> int:
        tmp = self.corpus.next
        while tmp != None and tmp.val not in self.set:
            tmp = tmp.next
        if tmp.next == None:
            return tmp.val
        self.corpus.next = tmp.next

        self.last.next = tmp
        self.last = tmp
        tmp.next = None
        return choice(list(self.set.keys()))
    def __str__(self):
        s = ''
        tmp = self.corpus
        while tmp != None:
            s+= str(tmp.val) + "-->"
            tmp = tmp.next
        return s
        
class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next
