class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.topDown(word1, word2)
    def sol1(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        # print(dp)
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    # print("i,j:",i,j,dp[i-1][j-1])
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j], dp[i][j-1]) + 1
        # print(dp)
        return dp[m][n]

    def bruteforce(self, s1: str, s2: str) -> int:
        def recur(i, j):
            if i == -1:
                return j+1
            if j == -1:
                return i+1
            if s1[i] == s2[j]:
                return recur(i-1, j-1)
            return 1 + min(
                recur(i, j-1),
                recur(i-1, j),
                recur(i-1, j-1)
            )
        return recur(len(s1)-1, len(s2)-1)

    def topDown(self, word1: str, word2: str) -> int:
        memo = {}
        def dp(i, j):
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1
            if (i,j) in memo:
                return memo[(i,j)]
            if word1[i] == word2[j]:
                memo[(i,j)] = dp(i-1, j-1)
                return memo[(i,j)]
            else:
                memo[(i,j)] = 1+ min(
                    dp(i-1, j),
                    dp(i, j-1),
                    dp(i-1, j-1)
                )
                return memo[(i,j)]
        return dp(len(word1)-1, len(word2)-1)