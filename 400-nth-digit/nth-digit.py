class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1
        count = 9
        while count * digit < n:
            n -= count * digit
            digit += 1
            count *= 10
        number = (count / 9) + (n-1) / digit
        index = (n-1) % digit
        return int(str(number)[index])
        