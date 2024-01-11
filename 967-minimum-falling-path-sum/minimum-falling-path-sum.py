class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        return self.topDown(matrix)

    def topDown(self, matrix):
        n = len(matrix)
        memo = [[inf]*n for _ in range(n)]
        def dp(i, j):
            if not (0 <= i < n) or not (0 <= j < n):
                return inf
            if i == 0:
                memo[i][j] = matrix[i][j]
                return memo[i][j]
            if memo[i][j] != inf:
                return memo[i][j]
            memo[i][j] = matrix[i][j] + min(dp(i-1, j-1), dp(i-1, j), dp(i-1, j+1))
            return memo[i][j]
        for j in range(n):
            dp(n-1, j)
        return min(memo[n-1])

    def downTop(self, matrix):
        n = len(matrix)
        dp = [x for x in matrix[0]]
        for i in range(1, n):
            temp = dp.copy()
            for j in range(0, n):
                mini = inf
                if j - 1 >= 0:
                    mini = min(mini, dp[j-1])
                if j + 1 < n:
                    mini = min(mini, dp[j+1])
                temp[j] = min(mini, dp[j]) + matrix[i][j]
            dp = temp
        return min(dp)
