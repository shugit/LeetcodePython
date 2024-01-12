class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.downTop(s, wordDict)

    def backtrack_naive(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        path = []
        res = []
        def backtrack(i):
            if i == len(s):
                res.append(" ".join(path))
            for w in words:
                if i + len(w) <= len(s) and s[i: i+ len(w)] == w:
                    path.append(w)
                    backtrack(i+len(w))
                    path.pop()
        backtrack(0)
        return res

    def topDown(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        path = []
        memo = {}
        def dp(i):
            if i == len(s):
                return [""]
            if i in memo:
                return memo[i]
            res = []
            for w in words:
                if i + len(w) <= len(s) and s[i: i+len(w)] == w:
                    suffixs = dp(i+len(w))
                    for suffix in suffixs:
                        if suffix == "":
                            res.append(w)
                        else:
                            res.append(w + " " + suffix)
            memo[i] = res
            return res
        return dp(0)

    def downTop(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [ [] for _ in range(len(s)+1)]
        dp[0] = [""]
        for i in range(0, len(s)+1):
            if dp[i]:
                for w in wordDict:
                    if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                        for prefix in dp[i]:
                            if prefix == "":
                                dp[i+len(w)].append(w)
                            else:
                                dp[i+len(w)].append(prefix +" " + w)
        return dp[len(s)]