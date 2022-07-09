class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt
class MyLinkedList:

    def __init__(self):
        self.linkedlist = Node(-1)
        self.len = 0
        self.tail = self.linkedlist

    def get(self, index: int) -> int:
        if index > self.len-1:
            return -1
        else:
            tmp = self.linkedlist
            for i in range(index):
                tmp = tmp.next
            return tmp.next.val

    def addAtHead(self, val: int) -> None:
        backup = self.linkedlist.next
        cur = Node(val,backup)
        self.linkedlist.next = cur
        self.len+=1
        if self.tail == self.linkedlist:
            self.tail = cur

    def addAtTail(self, val: int) -> None:
        cur = Node(val)
        self.tail.next = cur
        self.tail = self.tail.next
        self.len+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return
        if index == self.len:
            self.addAtTail(val)
        else:
            tmp = self.linkedlist
            for i in range(index):
                tmp = tmp.next
            backup = tmp.next
            cur =  Node(val, backup)
            tmp.next = cur
            self.len+=1
            

    def deleteAtIndex(self, index: int) -> None:
        if index <= self.len-1:
            tmp = self.linkedlist
            for i in range(index):
                tmp = tmp.next
            tmp.next = tmp.next.next
            if index == self.len-1:
                self.tail = tmp
            self.len-=1
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)