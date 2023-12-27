class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == n == 1:
            return grid[0][0]
        res = grid[m-1][n-1]
        q = [(grid[0][0],0,0)]
        visited = set()
        while q:
            h,i,j = heapq.heappop(q)
            res = max(h, res)
            if i == m-1 and j == n-1:
                return res
            if (i,j) in visited:
                continue
            visited.add((i,j))
            for stepI, stepJ in [[1,0],[-1,0],[0,1],[0,-1]]:
                newI,newJ = stepI+i, stepJ+j
                if 0 <= newI < m and 0 <= newJ < n and (newI, newJ) not in visited:
                    heapq.heappush(q, [grid[newI][newJ], newI, newJ])
        return res
