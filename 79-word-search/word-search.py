class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = []
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def bt(curStr, i, prev_m, prev_n):
            if curStr == word:
                return True
            if i >= len(word):
                return False
            for dire in directions:
                m = prev_m + dire[0]
                n = prev_n + dire[1]
                if m < 0 or n < 0 or m >= len(board) or n >= len(board[m]):
                    continue
                if board[m][n] != None and board[m][n] == word[i]:
                    board[m][n] = None
                    res = bt(curStr+word[i], i+1, m, n)
                    if res:
                        return True
                    board[m][n] = word[i]
        for m in range(len(board)):
            for n in range(len(board[m])):
                if board[m][n] == word[0]:
                    board[m][n] = None
                    res = bt(word[0],1,m,n)
                    if res:
                        return True
                    board[m][n] = word[0]
        return False

