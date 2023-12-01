class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
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