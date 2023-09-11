class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        for i in range(1, n+1):
            for j in range(0,i):
                cur = s[j:i] 
                if dp[i] is True:
                    break
                else:
                    dp[i] = dp[j] and cur in wordDict

        return dp[n]
