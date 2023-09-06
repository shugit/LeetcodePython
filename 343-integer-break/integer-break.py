class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}
        dp[1] = 1
        dp[2] = 2
        for num in range(2, n+1):
            dp[num] = 0 if num == n else num
            for i in range(1, num//2+1):
                product = dp[num-i] * dp[i]
                dp[num]  = max(dp[num], product)
        return dp[n]




        def dfs(num):
            if num in dp:
                return dp[num]
            dp[num] = 0 if num==n else num
            for i in range(1,num):
                product = dfs(i) * dfs(num-i)
                dp[num] = max(dp[num], product)
            return dp[num]
        return dfs(n)