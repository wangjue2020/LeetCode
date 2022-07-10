class MinStack:

    def __init__(self):
        self.l = []
        self.minl = []
    def push(self, val: int) -> None:
        self.l.append(val) 
        if self.minl == []:
            self.minl.append(val)
        else:
            if val <= self.minl[-1]:
                self.minl.append(val)

    def pop(self) -> None:
        cur = self.l.pop()
        if cur == self.minl[-1]:
            self.minl.pop()
    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.minl[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()