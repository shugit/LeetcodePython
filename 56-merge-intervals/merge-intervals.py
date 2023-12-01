class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        s,e = -1,-1
        res = []
        for i, (left, right) in enumerate(intervals):
            if e < left:
                res.append([s,e])
                s, e = left, right
            elif s > right:
                res.append([left,right])
            else:
                s = min(left, s)
                e = max(right,e)
        res.append([s,e])
        return res[1:]