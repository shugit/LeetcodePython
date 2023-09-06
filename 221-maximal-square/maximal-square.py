class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        maxi = 0
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0 :
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    maxi = max(dp[i][j], maxi)
        print(dp)
        return maxi*maxi