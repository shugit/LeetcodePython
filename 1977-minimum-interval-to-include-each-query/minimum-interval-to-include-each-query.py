class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sortQ = sorted(queries)
        res = {}
        minHeap = []
        i = 0
        for q in sortQ:
            while i < len(intervals):
                left = intervals[i][0]
                right = intervals[i][1]
                if left > q:
                    break
                size = right - left + 1
                heapq.heappush(minHeap, (size, right))
                i += 1
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
            
        return [res[x] for x in queries]
            

