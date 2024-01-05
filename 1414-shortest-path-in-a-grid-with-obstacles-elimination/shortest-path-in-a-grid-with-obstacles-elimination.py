class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if k >= m + n - 2:
            return m + n - 2
        q = deque([(0, 0, 0)])
        visited = set([(0, 0, 0)])
        step = 0
        while q:
            for _ in range(len(q)):
                i, j, used = q.popleft()
                if i == m-1 and j == n-1:
                    return step
                for di, dj in [[1,0], [-1,0], [0,1], [0,-1]]:
                    ni, nj = di + i, dj + j
                    if 0 <= ni < m and 0 <= nj < n:
                        if grid[ni][nj] == 0 and (ni, nj, used) not in visited:
                            visited.add((ni, nj, used))
                            q.append([ni, nj, used])
                        elif grid[ni][nj] == 1 and used < k and (ni, nj, used+1) not in visited:
                            visited.add((ni, nj, used + 1))
                            q.append([ni, nj, used + 1]) 
            step += 1
        return -1
