class Solution:
    def minMeetingRooms2(self, intervals: List[List[int]]) -> int:
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

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) <=1 :
            return len(intervals)
        s = []
        e = []
        for l, r in intervals:
            s.append(l)
            e.append(r)
        s.sort()
        e.sort()
        i, j = 0,0
        maxi = -inf
        count = 0
        while i < len(s):
            if s[i] < e[j]:
                count += 1
                maxi = max(maxi, count)
                i += 1
            else:
                count -= 1
                j += 1
        return maxi
