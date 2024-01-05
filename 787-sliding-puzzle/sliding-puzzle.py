class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def findZero(board):
            for ri in range(len(board)):
                for rj in range(len(board[ri])):
                    if board[ri][rj] == 0:
                        return ri, rj
        i, j = findZero(board)
        q = deque([(i, j, board)])
        visited = set("".join(["".join(map(str,row)) for row in board]))
        step = 0
        while q:
            for _ in range(len(q)):
                (i, j, board) = q.popleft()
                if board == [[1,2,3],[4,5,0]]:
                    return step
                for di,dj in [[1,0],[-1,0],[0,1],[0,-1]]:
                    ni, nj =  i + di, j + dj
                    if 0 <= ni < 2 and 0 <= nj < 3 :
                        newBoard = [row[:] for row in board]
                        newBoard[i][j], newBoard[ni][nj] = newBoard[ni][nj], newBoard[i][j]
                        boardStr = "".join(["".join(map(str,row)) for row in newBoard])
                        if boardStr not in visited:
                            visited.add(boardStr)
                            q.append([ni, nj, newBoard]) 
            step += 1
        return -1
        
                
                