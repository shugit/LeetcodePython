class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        return self.prim(points)

    def kruskal(self, points):
        return


    def prim(self, points):
        n = 0
        q = [(0,0)]
        visited = [False] * len(points)
        res = 0

        while n < len(points):
            w, curr = heapq.heappop(q)
            if visited[curr]:
                continue
            visited[curr] = True
            res += w
            n += 1
            cur_p = points[curr]
            for i, p in enumerate(points):
                if not visited[i]:
                    # print(i,p, cur_p)
                    next_w = abs(p[0] - cur_p[0]) + abs(p[1] - cur_p[1])
                    heapq.heappush(q, (next_w, i))
                    # print(q)
        return res