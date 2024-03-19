class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                d[i+j].append(mat[i][j])
        res = []
        for key, value in d.items():
            if key % 2 == 0:
                res += value[::-1]
            else:
               res += value
        return res