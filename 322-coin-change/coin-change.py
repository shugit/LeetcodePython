class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.sol1(coins, amount)

    def sol2(self, coins, amount):
        memo = {0:0}
        def dp(n):
            if n in memo:
                return memo[n]
            if n < 0:
                return -1
            res = inf
            for coin in coins:
                sub = dp(n-coin)
                if sub == -1:
                    continue
                res = min(res, sub+1)
            memo[n] = res if res != inf else -1
            return memo[n]
        return dp(amount)

    def sol1(self, coins, amount):
        dp =  [inf for _ in range(amount + 1)]
        
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] != inf else -1