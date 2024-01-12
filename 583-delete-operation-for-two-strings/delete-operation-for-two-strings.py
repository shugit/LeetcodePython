class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.topDown(word1, word2)
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
        return 0