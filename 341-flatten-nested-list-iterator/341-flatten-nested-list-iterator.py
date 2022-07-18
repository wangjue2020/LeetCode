# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        self.l = []
        self.ind = 0
        self.flattenList(nestedList)
    def flattenList(self, nested_list):
        for e in nested_list:
            if e.isInteger():
                self.l.append(e.getInteger())
            else:
                self.flattenList(e.getList())
    def next(self) -> int:
        self.ind+=1
        return self.l[self.ind-1]
    def hasNext(self) -> bool:
        return self.ind < len(self.l)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())