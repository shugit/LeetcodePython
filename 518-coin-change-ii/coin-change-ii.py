class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.downTop(amount, coins)

    def downTop(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount+1) for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0] = 1
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if j-coins[i-1] >= 0:
                    dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(coins)][amount]





    def sol1(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [ [0 for _ in range(amount + 1)] for _ in range(n + 1) ]
      
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1,n+1):
            cur = coins[i-1]
            for j in range(0, amount+1):
                if cur > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j - cur] + dp[i-1][j]
        print(dp)
        return dp[n][amount]

    def sol2(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
            print(dp)

        return dp[amount]