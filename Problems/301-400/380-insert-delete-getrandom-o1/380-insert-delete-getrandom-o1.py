from random import choice
class RandomizedSet:

    def __init__(self):
        self.set = {}

    def insert(self, val: int) -> bool:
        cur = self.set.get(val)
        if cur is None:
            self.set[val] = val
            return True
        else:
            return False
    def remove(self, val: int) -> bool:
        cur = self.set.get(val)
        if cur is None:
            return False
        else:
            del self.set[val]
            return True
        

    def getRandom(self) -> int:
        return choice(list(self.set.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()