class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if board[i][j] != "O":
                return
            board[i][j] = "T"
            for x,y in directions:
                new_i = x + i 
                new_j = y + j
                dfs(new_i,new_j) 
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O" 
        return