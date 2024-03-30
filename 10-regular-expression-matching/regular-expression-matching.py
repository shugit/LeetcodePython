class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = defaultdict(lambda: False)
        dp[(len(s),len(p))] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):
                if j + 1 < len(p) and p[j+1] == "*":
                    dp[(i,j)] = dp[(i, j + 2)]
                    if i < len(s) and s[i] == p[j] or p[j] == ".":
                        dp[(i,j)] = dp[(i+1,j)] or dp[(i, j)]
                elif i < len(s) and s[i] == p[j] or p[j] == ".":
                    dp[(i,j)] = dp[(i+1, j + 1)]
        return dp[(0,0)]
        