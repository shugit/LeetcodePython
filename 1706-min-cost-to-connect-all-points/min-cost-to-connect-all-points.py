class UnionFind:
    def __init__(self, size):
        self.group = [i for i in range(size)]
        self.rank = [0] * size

    def join(self, i, j):
        g1 = self.find(i)
        g2 = self.find(j)
        if g1 == g2:
            return False
        if self.rank[g1] > self.rank[g2]:
            self.group[g2] = g1
        elif self.rank[g1] < self.rank[g2]:
            self.group[g1] = g2
        else:
            self.group[g1] = g2
            self.rank[g2] += 1
        return True


    def find(self, node):
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # return self.prim(points)
        return self.kruskal(points)

    def kruskal(self, points):
        g = []
        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points):
                if i != j:
                    w = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                    g.append([w, i, j])
        g.sort()
        # print(g)
        uf = UnionFind(len(points))
        res = 0
        n = 0
        for w, i, j in g:
            if uf.join(i,j):
                res += w
                n += 1
                if n == len(points) - 1:
                    break
        return res


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
                    next_w = abs(p[0] - cur_p[0]) + abs(p[1] - cur_p[1])
                    heapq.heappush(q, (next_w, i))
        return res