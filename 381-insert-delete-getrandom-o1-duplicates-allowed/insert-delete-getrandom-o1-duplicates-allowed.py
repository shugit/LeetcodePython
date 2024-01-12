class RandomizedCollection:
    def __init__(self):
        self.h = defaultdict(set)
        self.arr = []

    def insert(self, val: int) -> bool:
        self.h[val].add(len(self.arr))
        self.arr.append(val)
        return len(self.h[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.h:
            return False
        idx = self.h[val].pop()
        self.arr[idx] = self.arr[-1]
        self.h[self.arr[idx]].add(idx)
        self.h[self.arr[idx]].remove(len(self.arr)-1)
        if len(self.h[val]) == 0:
            del self.h[val]
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()