# from collections import defaultdict
from sortedcontainers import SortedDict
class MyCalendarTwo:

    def __init__(self):
        self.books = SortedDict()

    def book(self, start: int, end: int) -> bool:
        if end in self.books:
            self.books[end] -= 1
        else:
            self.books[end] = -1
        if start in self.books:
            self.books[start] += 1
        else:
            self.books[start] = 1
        prefix = 0
        for key,value in self.books.items():
            prefix += value
            if prefix >= 3:
                self.books[start] -= 1
                self.books[end] += 1
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)