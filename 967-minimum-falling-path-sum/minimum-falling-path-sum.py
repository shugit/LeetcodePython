class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
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
