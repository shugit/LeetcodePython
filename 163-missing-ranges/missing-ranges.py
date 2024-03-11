class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        s = lower
        res = []
        for n in nums + [upper+1]:
            if n > s:
                res.append([s, n-1])
            s = n + 1
        return res

