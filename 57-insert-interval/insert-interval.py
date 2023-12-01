class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s = newInterval[0]
        e = newInterval[1]
        res = []
        for i,(left,right) in enumerate(intervals):
            if e < left:
                res.append([s,e])
                return res + intervals[i:]
            elif s > right:
                res.append([left,right])
            else:
                s = min(left, s)
                e = max(right, e)
        res.append([s,e])
        return res
            
