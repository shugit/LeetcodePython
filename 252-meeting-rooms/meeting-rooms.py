class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        if not intervals:
            return True
        s, e = intervals[0]
        for i, (left, right) in enumerate(intervals[1:]):
            if e <= left:
                s,e = left, right
            else:
                return False
        return True