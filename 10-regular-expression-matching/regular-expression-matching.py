class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < len(p) and p[j + 1] == "*": #the first char in pattern string is never going to be '*
                        # don't use "*"
                cache[(i, j)] = (dfs(i, j + 2)) or (match and dfs(i + 1, j)) 
                                             # use "*", and we can only use "*" if there is match
                return cache[(i, j)]
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            
            cache[(i, j)] = False
            return False
            
        return dfs(0, 0)