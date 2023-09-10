class Solution:
    def numSquares(self, n: int) -> int:
        arr = []
        for i in range(0, n+1):
            if i*i <= n:
                arr.append(i*i)
        size = len(arr)
        dp = [float("inf") for _ in range(n+1)]
        dp[0] = 0
        # print(arr)
        for i in range(1, size + 1):
            cur = arr[i-1]
            for j in range(1, n+1):
                if j - cur >= 0 :
                    dp[j] = min(dp[j], dp[j-cur]+1)
            # print(dp)
        return dp[n]