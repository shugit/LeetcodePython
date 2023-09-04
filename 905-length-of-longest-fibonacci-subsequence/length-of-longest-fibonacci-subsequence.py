class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        dp = [ [0 for j in range(n)] for i in range(n)]
        h = {}
        maxi = 0
        for i in range(n):
            h[arr[i]] = i
            
        for i in range(n):
            for j in range(i + 1, n):
                if dp[i][j] == 0:
                    dp[i][j] = 2
                val_k = arr[i] + arr[j] 
                if val_k in h:
                    k = h[val_k]
                    # print(dp[i][j]))
                    dp[j][k] = max(dp[j][k], dp[i][j] + 1)
                    maxi = max(maxi, dp[j][k])
        if maxi >= 3:
            return maxi
        return 0