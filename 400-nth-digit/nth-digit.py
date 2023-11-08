class Solution:
    def findNthDigit(self, n: int) -> int:
        base = digit = 1
        while n > 9 * base * digit:
            n -= 9 * base * digit
            digit += 1
            base *= 10
        q, r = divmod(n-1, digit)
        return int(str(base+q)[r])
        