class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        res = set()
        m, n = len(grid), len(grid[0])
        def dfs(i, j, pi, pj):
            path.append([pi,pj])
            for di, dj in [[1,0], [-1,0], [0,1], [0,-1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    grid[ni][nj] = 0
                    dfs(ni, nj, di,dj)
            path.append([-pi, -pj])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    path = []
                    dfs(i, j, 0, 0)
                    # print(i,j, path)
                    res.add(" ".join(["".join(map(str, row)) for row in path]))
        # print(res)
        return len(res)
