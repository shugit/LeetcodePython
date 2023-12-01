class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) <=1 :
            return len(intervals)
        count = 1
        maxi = 1
        h = defaultdict(int)
        for left, right in intervals:
            h[left] += 1
            h[right] -= 1
        prefix = 0
        maxi = -inf
        for i,val in sorted(h.items()):
            prefix += val
            maxi = max(prefix, maxi)
        return maxi
