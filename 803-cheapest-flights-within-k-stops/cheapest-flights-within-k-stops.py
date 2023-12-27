class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0
        return self.bellmanFord(n, flights, src, dst, k)

    def bellmanFord(self, n, flights, src, dst, k):
        prev = [inf] * n
        cur = [inf] * n
        prev[src] = 0
        for i in range(1, k + 2):
            cur[src] = 0
            for f,t,p in flights:
                if prev[f] < inf:
                    cur[t] = min(cur[t], prev[f] + p)
            # print("\t".join(map(str,cur)))
            prev = cur.copy()
        return -1 if cur[dst] == inf else cur[dst]

            