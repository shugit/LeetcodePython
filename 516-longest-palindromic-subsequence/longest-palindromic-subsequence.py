class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        size = len(s)
        dp = [ [0 for _ in range(size+1)] for _ in range(size+1)]
        for length in range(1, size+1):
            limit = size - length + 1
            for i in range(0, limit):
                j = i + length - 1
                # print("length=",length,"i=",i,"/",limit-1, "j=",j)
                if j == i:
                    dp[i][j] = 1
                    continue
                if s[j] == s[i]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        # print(dp)
        return dp[0][size-1]