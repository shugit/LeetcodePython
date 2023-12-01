class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        state = [["."] * n for _ in range(n)]  # Start with an empty board
        res = []

        visited_cols = set()
        visited_diagonals = set()
        visited_antidiagonals = set()

        def backtrack(row):
            if row == n:
                res.append(["".join(row) for row in state])
                return

            for col in range(n):
                diagonal_difference = row - col
                diagonal_sum = row + col

                if not (col in visited_cols or
                        diagonal_difference in visited_diagonals or
                        diagonal_sum in visited_antidiagonals):

                    visited_cols.add(col)
                    visited_diagonals.add(diagonal_difference)
                    visited_antidiagonals.add(diagonal_sum)
                    state[row][col] = 'Q'
                    backtrack(row + 1)

                    visited_cols.remove(col)
                    visited_diagonals.remove(diagonal_difference)
                    visited_antidiagonals.remove(diagonal_sum)
                    state[row][col] = '.'

        backtrack(0)
        return res
        # Please Upvote me 