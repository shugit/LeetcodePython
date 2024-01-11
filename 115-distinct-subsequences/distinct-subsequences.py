class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        memo = {}
        def dp(i, j):
            if j == len(t):
                return 1
            if len(s) - i < len(t) - j:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            res = 0
            for k in range(i, len(s)):
                if s[k] == t[j]:
                    res += dp(k+1, j+1)
            memo[(i,j)] = res
            return res
        dp(0,0)
        return memo[(0,0)]