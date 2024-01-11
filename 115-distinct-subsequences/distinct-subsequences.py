class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return self.sol_s(s,t)
    def sol_s(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        def dp(i,j):
            if j == len(t):
                return 1
            if len(s) - i < len(t) - j:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            res = 0
            if s[i] == t[j]:
                res += dp(i+1, j+1) + dp(i+1, j)
            else:
                res += dp(i+1, j)
            memo[(i,j)] = res
            return res
        memo = {}
        dp(0,0)
        return memo[(0,0)] 



    def sol_t(s, t):
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