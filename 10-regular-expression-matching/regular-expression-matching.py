class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = [[-1] * (len(p)+1) for _ in range(len(s)+1)]
        def dp(i, j):
            if memo[i][j] != -1:
                return memo[i][j]
            if j == len(p):
                memo[i][j] = (i == len(s))
                return memo[i][j]
            if i == len(s):
                memo[i][j] = True
                if (len(p) - j) % 2 == 1:
                    memo[i][j] = False
                for k in range(j+1, len(p), 2):
                    if p[k] != "*":
                        memo[i][j] = False
                return memo[i][j]
            res = False
            if s[i] == p[j] or p[j] == '.':
                if j < len(p) - 1 and p[j+1] == "*":
                    res = dp(i, j + 2) or dp(i + 1, j)
                else:
                    res = dp(i + 1, j + 1)
            else:
                if j < len(p) - 1 and p[j+1] == "*":
                    res = dp(i, j + 2)
                else:
                    res = False
            memo[i][j] = res
            return memo[i][j]
        dp(0, 0)
        return memo[0][0]

            
