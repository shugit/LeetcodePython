class Solution:
    def minSteps(self, n: int) -> int:
        dp = {}
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n+1): 
            dp[i] = i
            for j in range(2,i//2+1):
                if i % j == 0:
                    dp[i] = min(dp[j] + i//j, dp[i])

        return dp[n]