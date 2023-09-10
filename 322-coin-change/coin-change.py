class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [ [float("inf") for _ in range(amount + 1)] for _ in range(n+1)]
        

        for i in range(1, n+1):
            cur = coins[i-1]
            dp[i][0] = 0
            for j in range(1, amount + 1):
                if j-cur >=0:
                    dp[i][j] = min(dp[i][j-cur] + 1, dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        # print(dp)
        if dp[n][amount] == float("inf"):
            return -1
        else:
            return dp[n][amount]
