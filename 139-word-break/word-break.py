class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        for i in range(1, n+1):
            for j in range(0,i):
                cur = s[j:i] #实际取到的是j~i-1，因为i从1开始，j从0开始，所以正好
                dp[i] = dp[j] and cur in wordDict
                if dp[i] is True:
                    break

        return dp[n]
