class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == n == 1:
            return 1 if obstacleGrid[0][0] == 0 else 0
        dp = [0] * n
        dp[0] = 1
        for i in range(0, m):
            temp = dp.copy()
            for j in range(0, n):
                if i == 0 and j == 0:
                    temp[0] = 1
                    continue
                if obstacleGrid[i][j] == 1:
                    temp[j] = 0 
                    continue
                left = temp[j-1] if j-1 >= 0 and obstacleGrid[i][j-1] != 1 else 0
                top = dp[j] if i-1>=0 and obstacleGrid[i-1][j] != 1  else 0
                temp[j] = left + top
            dp = temp
        return dp[n-1]