import heapq
class LFUCache:
    def __init__(self, capacity: int):
        self.keyToVal = {}
        self.keyToFreq = {}
        self.freqToKeys = defaultdict(list)
        self.cap = capacity
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key not in self.keyToVal:
            return -1
        self.increaseFreq(key)
        return self.keyToVal[key]

    def put(self, key: int, value: int) -> None:
        if key in self.keyToVal:
            self.keyToVal[key] = value
            self.increaseFreq(key)
            return
        if self.cap <= len(self.keyToVal):
            self.removeMinFreqKey()
        self.keyToVal[key] = value
        self.keyToFreq[key] = 1
        self.freqToKeys[1].append(key)
        self.minFreq = 1

    def removeMinFreqKey(self):
        keys = self.freqToKeys[self.minFreq]
        toDelKey = keys.pop(0)
        if not keys:
            del self.freqToKeys[self.minFreq]
        del self.keyToVal[toDelKey]
        del self.keyToFreq[toDelKey]
    
    def increaseFreq(self, key):
        freq = self.keyToFreq[key]
        self.keyToFreq[key] += 1
        self.freqToKeys[freq].remove(key)
        self.freqToKeys[freq+1].append(key)
        if not self.freqToKeys[freq]:
            del self.freqToKeys[freq]
            if freq == self.minFreq:
                self.minFreq += 1