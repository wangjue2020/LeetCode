from random import choice
class RandomizedSet:

    def __init__(self):
        self.set = {}
    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.set[val] = val

        return True
    def remove(self, val: int) -> bool:
        if val in self.set:
            del self.set[val]
            return True
        return False
        
    def getRandom(self) -> int:

        return choice(list(self.set.keys()))

