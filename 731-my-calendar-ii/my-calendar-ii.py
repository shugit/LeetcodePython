# from collections import defaultdict
class MyCalendarTwo:

    def __init__(self):
        self.books = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        self.books[end] -= 1
        self.books[start] += 1
        sort_book = sorted(self.books)
        prefix = 0
        for key in sort_book:
            prefix += self.books[key]
            if prefix >= 3:
                self.books[start] -= 1
                self.books[end] += 1
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)