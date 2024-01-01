class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        min1 = min2 = 0
        idx1 = idx2 = -1
        for c in costs:
            curMin1 = curMin2 = inf
            curIdx1 = curIdx2 = -1
            for j in range(0, len(c)):
                if j == idx1:
                    curC = c[j] + min2
                else:
                    curC = c[j] + min1
                if curC < curMin1:
                    curMin1, curMin2 = curC, curMin1
                    curIdx1, curIdx2 = j, curIdx1
                elif curC <= curMin2:
                    curMin2, curIdx2 = curC, j
            # print(curMin1, curMin2, curIdx1, curIdx2)
            min1, min2 = curMin1, curMin2
            idx1, idx2 = curIdx1, curIdx2
        return min1