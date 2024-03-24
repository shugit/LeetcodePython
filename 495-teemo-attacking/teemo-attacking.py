class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        s, e = 0, 0
        res = 0
        for l in timeSeries:
            if l > e:
                res += (e - s)
                s, e = l, l + duration
            elif s <= l <= e:
                e = max(e, l + duration)
        res += (e - s)
        return res
