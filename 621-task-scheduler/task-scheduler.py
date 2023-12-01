class Solution:
    def leastInterval2(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        freq = Counter(tasks)
        max_freq = max(freq.values())
        freq = list(freq.values())
        max_freq_count = 0
        for v in freq:
            if v == max_freq:
                max_freq_count += 1
        res = (max_freq-1) * (n+1) + max_freq_count
        return max(res, len(tasks))

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        frequencies = Counter(tasks)
        q = sorted(frequencies.values())

        # max frequency
        f_max = q.pop()
        idle_time = (f_max - 1) * n
        
        while q and idle_time > 0:
            idle_time -= min(f_max - 1, q.pop())
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)