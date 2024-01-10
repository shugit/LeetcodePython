class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x:x[1])
        count = 1
        e = points[0][1]
        for p in points:
            if p[0] > e:
                count += 1
                e = p[1]
        return count