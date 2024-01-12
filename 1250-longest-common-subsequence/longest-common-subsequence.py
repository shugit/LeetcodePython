class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.topDown(text1, text2)
    def topDown(self, text1: str, text2: str) -> int:
        memo = {}
        def dp(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + dp(i+1, j+1)
                return memo[(i, j)]
            else:
                res =  max(dp(i+1, j),
                            dp(i, j+1))
                memo[(i, j)] = res
                return memo[(i, j)]
        return dp(0,0)




    def downTop(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [ [0 for _ in range(n+1) ] for i in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[m][n]
