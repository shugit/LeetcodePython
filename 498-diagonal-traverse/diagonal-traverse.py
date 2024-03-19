class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = {}
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i + j not in d:
                    d[i+j] = [mat[i][j]]
                else:
                    d[i+j].append(mat[i][j])
        res = []
        for key, value in d.items():
            if key % 2 == 0:
                res += value[::-1]
            else:
               res += value
        return res