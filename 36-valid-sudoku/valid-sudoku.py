class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(n):
            h = set()
            for j in range(n):
                if board[i][j] == ".":
                    continue
                if  board[i][j] in h:
                    print("1", i,j)
                    return False
                h.add(board[i][j])
        for i in range(n):
            h = set()
            for j in range(n):
                if board[j][i] == ".":
                    continue
                if board[j][i] in h:
                    print("2", i,j)
                    return False
                h.add(board[j][i])
        for offset_i in range(0,3):
            for offset_j in range(0,3):
                h = set()
                for inner_i in range(0,3):
                    for inner_j in range(0,3):
                        i = offset_i*3 + inner_i
                        j = offset_j*3 + inner_j
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in h:
                            # print("3:", i,j, h)
                            return False
                        h.add(board[i][j])
                        # print(h)
        return True