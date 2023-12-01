class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        if not intervals:
            return True
        # print(intervals)
        for i in range(1, len(intervals)):
            # print(i,intervals[i-1], intervals[i])
            if intervals[i-1][1] > intervals[i][0]:
                return False
        return True