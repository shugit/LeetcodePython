class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.downTop(word1, word2)
    def topDown(self, word1: str, word2: str) -> int:
        memo = {}
        def dp(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j) in memo:
                return memo[(i,j)]
            if word1[i] == word2[j]:
                memo[(i,j)] = dp(i+1, j+1)
                return memo[(i,j)]
            else:
                memo[(i,j)] = 1 + min(dp(i+1, j), dp(i, j+1))
                return memo[(i,j)]
        return dp(0,0)


    def downTop(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2)+1) for _ in range(len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            dp[i][0] = i
        for j in range(1, len(word2) + 1):
            dp[0][j] = j
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        return dp[len(word1)][len(word2)]