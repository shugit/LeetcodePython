class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.preSum = copy.deepcopy(matrix)
        for j in range(1, n):
            self.preSum[0][j] += self.preSum[0][j-1]
        for i in range(1, m):
            self.preSum[i][0] += self.preSum[i-1][0]
            for j in range(1, n):
                self.preSum[i][j] += self.preSum[i-1][j] + self.preSum[i][j-1] - self.preSum[i-1][j-1]
        print(self.preSum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = self.preSum[row2][col1 - 1] if col1 > 0 else 0
        top = self.preSum[row1 - 1][col2] if row1 > 0 else 0
        over = self.preSum[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return self.preSum[row2][col2] - left - top + over


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)