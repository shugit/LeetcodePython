class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        def dfs(i, j, index):
            grid[i][j] = index
            area = 1
            for di, dj in [[1,0], [-1,0], [0,1],[0,-1]]:
                ni, nj = di+i, dj+j
                if 0 <= ni < m and 0 <= nj < m and grid[ni][nj] == 1:
                    area += dfs(ni, nj, index)
            return area
        area = {}
        index = 2
        for i in range(m):
           for j in range(m):
               if grid[i][j] == 1:
                   area[index] = dfs(i,j, index)
                   index += 1
        print(grid, area)
        maxi = max(area.values() or [0])
        for i in range(m):
           for j in range(m):
               if grid[i][j] == 0:
                    visited = set()
                    area_size = 1
                    for di, dj in [[1,0], [-1,0], [0,1],[0,-1]]:
                        ni, nj = di+i, dj+j
                        if 0 <= ni < m and 0 <= nj < m and grid[ni][nj] > 1:
                            index = grid[ni][nj]
                            if grid[ni][nj] not in visited:
                                visited.add(index)
                                area_size += area[index]
                    maxi = max(maxi, area_size) 
        return maxi