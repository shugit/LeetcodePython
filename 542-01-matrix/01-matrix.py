class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        res = [[-1] * n for _ in range (m)]
        q = deque([])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append([i,j])
                    res[i][j] = 0
        while q:
            (i, j) = q.popleft()
            for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
                si, sj = i + di, j + dj
                if 0 <= si < m and 0 <= sj < n and res[si][sj] == -1:
                    q.append([si,sj])
                    res[si][sj] = res[i][j] + 1
        return res