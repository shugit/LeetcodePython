class MovingAverage:
    def __init__(self, size: int):
        self.queue = deque([])
        self.size = size
        self.count = 0
        self.preSum = 0

    def next(self, val: int) -> float:
        if len(self.queue) < self.size:
            self.preSum += val
            self.queue.append(val)     
        else:
            n = self.queue.popleft()
            self.queue.append(val)
            self.preSum = self.preSum - n + val
        return 1.0 * self.preSum/len(self.queue)
        