class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}
        
        def dfs(num):
            if num in dp:
                return dp[num]
            dp[num] = 0 if num==n else num
            for i in range(1,num):
                product = dfs(i) * dfs(num-i)
                dp[num] = max(dp[num], product)
            return dp[num]
        return dfs(n)