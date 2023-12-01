class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.']*n for _ in range(n)]
        col = set()
        diag = set()
        r_diag = set()
        def bt(i):
            if i == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for j in range(n):
                if j in col or (i+j) in diag or (i-j) in r_diag:
                    continue
                col.add(j)
                diag.add(i+j)
                r_diag.add(i-j)
                board[i][j] = "Q"
                bt(i+1)
                col.remove(j)
                diag.remove(i+j)
                r_diag.remove(i-j)
                board[i][j] = '.'
        bt(0)
        return res