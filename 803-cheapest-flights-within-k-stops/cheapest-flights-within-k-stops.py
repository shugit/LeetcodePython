class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0
        # return self.bellmanFord(n, flights, src, dst, k)
        return self.bellmanFordImproved(n, flights, src, dst, k)

    def bellmanFord(self, n, flights, src, dst, k):
        prev = [inf] * n
        cur = [inf] * n
        prev[src] = 0
        g = defaultdict(list)
        for i in range(1, k + 2):
            cur[src] = 0
            for f,t,p in flights:
                if prev[f] < inf:
                    cur[t] = min(cur[t], prev[f] + p)
            # print("\t".join(map(str,cur)))
            prev = cur.copy()
        return -1 if cur[dst] == inf else cur[dst]

    def bellmanFordImproved(self, n, flights, src, dst, k):
        g = defaultdict(list)
        for f, t, p in flights:
            g[f].append((t,p))
        q = deque()
        q.append((0, src, 0)) #stop, from node, cost total
        dp = [inf] * n
        dp[src] = 0
        while q:
            stop, node, price = q.popleft()
            for nextNode, cost in g[node]:
                if dp[nextNode] > cost + price and stop <= k :
                    dp[nextNode] = cost + price
                    q.append((stop+1, nextNode, cost + price))
            print(dp)
        return -1 if dp[dst] == inf else dp[dst]