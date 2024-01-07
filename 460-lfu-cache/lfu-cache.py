import heapq

class LFUCache:
    def __init__(self, capacity):
        self.keyToVal = {} #key: (freq, value)
        self.freqs = defaultdict(OrderedDict)
        self.minFreq = 0
        self.cap = capacity

    def get(self, key) -> int:
        if key not in self.keyToVal:
            return -1
        self.update(key)
        return self.keyToVal[key][1]

    def put(self, key, value) -> None:
        if key not in self.keyToVal and self.cap == len(self.keyToVal):
            toDelKey = self.freqs[self.minFreq].popitem(False)
            del self.keyToVal[toDelKey[0]]
        if key in self.keyToVal:
            self.keyToVal[key][1] = value
            self.update(key)
            self.minFreq = min(self.minFreq, self.keyToVal[key][0])
        else:
            self.keyToVal[key] = [1, value]
            self.freqs[1][key] = None
            self.minFreq = 1
            

    def update(self, key):
        f, value = self.keyToVal[key]
        self.freqs[f].pop(key)
        self.freqs[f+1][key] = None
        if not self.freqs[f] and f == self.minFreq:
            self.minFreq += 1
        self.keyToVal[key][0] += 1
        

class LFUCache2:
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