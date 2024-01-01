class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        m,n = len(costs), len(costs[0])
        dp = [[0]*n for _ in range(m)]
        dp[0] = costs[0]
        # print(dp[0])
        for i in range(1, len(costs)):
            dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = costs[i][2] + min(dp[i-1][1], dp[i-1][0])
            # print(dp[i])
        return min(dp[m-1])