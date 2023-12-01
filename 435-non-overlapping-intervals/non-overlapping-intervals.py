class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0], x[1]))
        s,e = intervals[0][0], intervals[0][1]
        # print(intervals)
        count = 0
        for i, (left, right) in enumerate(intervals[1:]):
            if e <= left:
                s,e = left, right
            elif e < right:
                count += 1
            else:
                count += 1
                s,e = left, right
        return count
