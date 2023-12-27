class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        g = defaultdict(list)
        q = [(0,k)]
        res = 0
        for s, t, w in times:
            g[s].append([t,w])
        while q:
            w, node = heapq.heappop(q)
            if node in visited:
                continue
            res = max(res, w)
            visited.add(node)
            if node in g:
                for (nextNode, nextW) in g[node]:
                    if nextNode not in visited:
                        heapq.heappush(q, [nextW+w, nextNode])
        if len(visited) != n:
            return -1
        return res
        