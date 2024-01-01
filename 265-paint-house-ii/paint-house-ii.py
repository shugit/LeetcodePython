class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        m, n = len(costs), len(costs[0])
        dp = [[0]*n for _ in range(m)]
        dp[0] = costs[0]
        for i in range(1, m):
            for j in range(0, n):
                m1 = min(dp[i-1][:j]) if j > 0 else inf
                m2 = min(dp[i-1][j+1:]) if j + 1 < n else inf
                dp[i][j] = costs[i][j] + min(m1, m2)
        return min(dp[m-1])