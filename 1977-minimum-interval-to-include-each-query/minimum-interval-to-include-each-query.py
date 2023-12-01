class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sortQ = sorted(queries)
        res = {}
        minHeap = []
        i = 0
        for q in sortQ:
            while i < len(intervals):
                if intervals[i][0] > q:
                    break
                size = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(minHeap, (size, intervals[i][1]))
                i += 1
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
            
        return [res[x] for x in queries]
            

