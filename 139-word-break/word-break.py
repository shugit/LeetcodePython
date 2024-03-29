class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # return self.topDown(s, wordDict)
        return self.downTop(s, wordDict)

    def downTop(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        for i in range(0, n+1):
            for w in words:
                if dp[i] == True and s[i:i+len(w)] == w:
                    dp[i+len(w)] = True
        # print(dp)
        return dp[n]

    def topDown(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memo = {}
        def dp(i):
            if i == len(s):
                memo[i] = True
                return True
            if i in memo:
                return memo[i]
            for j in range(i+1, len(s)+1):
                if s[i:j] in words:
                    if dp(j):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dp(0)