class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        h = Counter(tasks)
        q = [-cnt for cnt in h.values()]
        heapq.heapify(q)
        print(q)
        time = 0
        dq = deque()
        while dq or q:
            time += 1
            if q:
                cnt = 1 + heapq.heappop(q)
                if cnt:
                    dq.append([cnt, time+ n])
            if dq and dq[0][1] == time:
                heapq.heappush(q, dq.popleft()[0])

        return time