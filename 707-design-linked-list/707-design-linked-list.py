class MyLinkedList:

    def __init__(self):
        self.list = []
        self.len = 0

    def get(self, index: int) -> int:
        if index > self.len-1:
            return -1
        else:
            return self.list[index]

    def addAtHead(self, val: int) -> None:
        self.list = [val] + self.list
        self.len += 1

    def addAtTail(self, val: int) -> None:
        self.list = self.list+[val]
        self.len+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < self.len:
            self.list.insert(index,val)
            self.len+=1
        if index == self.len:
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        if index <= self.len-1:
            self.list.pop(index)
            self.len-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)