class MovingAverage:
    def __init__(self, size: int):
        self.queue = deque([])
        self.size = size
        self.count = 0

    def next(self, val: int) -> float:
        if len(self.queue) < self.size:
            self.queue.append(val)     
        else:
            self.queue.popleft()
            self.queue.append(val)
        return 1.0 * sum(self.queue)/len(self.queue)
        