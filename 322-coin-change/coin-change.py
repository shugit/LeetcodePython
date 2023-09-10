class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp =  [float("inf") for _ in range(amount + 1)]
        
        dp[0] = 0
        for i in range(1, n+1):
            cur = coins[i-1]
            for j in range(1, amount + 1):
                if j-cur >= 0:
                    dp[j] = min(dp[j-cur] + 1, dp[j])
        # print(dp)
        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]
