class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        g = [[0] * k for k in range(1, 102)]
        g[0][0] = poured
        for i in range(query_row+1):
            for j in range(i+1):
                q = (g[i][j] - 1.0) / 2.0
                if q > 0:
                    g[i+1][j] += q
                    g[i+1][j+1] += q
        k = g[query_row][query_glass]
        return min(1, k)

