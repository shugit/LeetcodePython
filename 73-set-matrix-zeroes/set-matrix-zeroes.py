class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        m_arr = [1] * m
        n_arr = [1] * n 
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    m_arr[i] = 0
                    n_arr[j] = 0
        # print(m_arr,n_arr)
        for i in range(0, m):
            for j in range(0, n):
                if m_arr[i] == 0 or n_arr[j] == 0:
                    matrix[i][j] = 0
        return 
                    