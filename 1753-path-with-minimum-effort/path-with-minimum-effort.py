class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        return self.kruskal(heights)
        # return self.minheap(heights)

    def kruskal(self, heights):
        m = len(heights)
        n = len(heights[0])
        if m == n == 1:
            return 0
        g = []
        for i in range(m):
            for j in range(n):
                if i + 1 < m:
                    w = abs(heights[i][j] - heights[i+1][j])
                    g.append([w, i*n+j, (i+1) * n + j])
                if j + 1 < n:
                    w = abs(heights[i][j] - heights[i][j+1])
                    g.append([w, i*n + j , i* n + j + 1])
        g.sort()
        # print(g)
        class UnionFind:
            def __init__(self, size):
                self.group = [i for i in range(size)]
                self.rank = [0] * size # size of each group

            def find(self, id):
                if self.group[id] != id:
                    self.group[id] = self.find(self.group[id])
                return self.group[id]

            def union(self, i, j):
                g1 = self.find(i)
                g2 = self.find(j)
                if g1 == g2:
                    return False
                if self.rank[g1] > self.rank[g2]:
                    self.group[g2] = g1
                elif self.rank[g1] < self.rank[g2]:
                    self.group[g1] = g2
                else:
                    self.group[g2] = g1
                    self.rank[g1] += 1
                return True

        uf = UnionFind(m*n)
        for w, p1, p2 in g:
            uf.union(p1, p2)
            if uf.find(0) == uf.find(m*n-1):
                return w
        return -1





        return 0
            



    def minheap(self, heights):
        return 0
