from sortedcontainers import SortedDict 
class MyCalendarThree:

    def __init__(self):
        self.d = SortedDict(int)

    def book(self, startTime: int, endTime: int) -> int:
        self.d[startTime] = self.d.get(startTime, 0) + 1
        self.d[endTime] = self.d.get(endTime,0) - 1
        prefix = 0
        cnt = 0
        for key, value in self.d.items():
            prefix += value
            cnt = max(cnt, prefix)
        return cnt


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)