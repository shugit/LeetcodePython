class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1
        count = 9
        st = 1
        while count * digit < n:
            n -= count * digit
            digit += 1
            count *= 10
            st *= 10
        st += (n-1)/digit
        st = str(st)
        return int(st[(n-1) % digit])
        