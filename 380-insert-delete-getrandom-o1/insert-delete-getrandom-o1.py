class RandomizedSet:

    def __init__(self):
        self.h = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.h:
            return False
        self.h[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.h:
            return False
        idx = self.h[val]
        last = self.arr[-1]
        self.arr[idx], self.arr[-1] = last, val
        self.h[last] = idx
        self.arr = self.arr[:-1]
        del self.h[val]
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()