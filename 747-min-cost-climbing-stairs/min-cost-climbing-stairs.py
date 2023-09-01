class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        n = len(cost)-1
        dp[0] = cost[0]
        dp[1] = cost[1]
        cost.append(0)
        i = 2
        while i <= n+1: 
            dp[i] = min(dp[i-2] + cost[i], dp[i-1] + cost[i])
            i += 1
        return min(dp[n+1], dp[n]+cost[n+1])