class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0],-x[1]) )
        s, e = intervals[0][0], intervals[0][1]
        removed = 0
        for left, right in intervals[1:]:
            if left >= s and right <= e:
                removed += 1
            else:
                s, e = min(s, left), max(e, right)
            
        return len(intervals) - removed
            