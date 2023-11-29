class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort(key=lambda x: (x[0], x[1]))
        print(ranges)
        for i in range(left, right + 1):
            inside = False
            for x,y in ranges:
                if x<=i<=y:
                    inside = True
                    break
            if not inside:
                return False

        return True