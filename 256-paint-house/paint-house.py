class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        m,n = len(costs), len(costs[0])
        dp = costs[0]
        for i in range(1, len(costs)):
            c1 = costs[i][0] + min(dp[1], dp[2])
            c2 = costs[i][1] + min(dp[0], dp[2])
            c3 = costs[i][2] + min(dp[1], dp[0])
            dp = [c1, c2, c3]
        return min(dp)