import heapq
class Solution:
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = []
        for i in range(k):
            t = (-nums[i],i) 
            heapq.heappush(q, t)
        res.append(-q[0][0])
        for i in range(k, len(nums)):
            while q and q[0][1] <= i-k:
                heapq.heappop(q)
            t = (-nums[i], i)
            heapq.heappush(q, t)
            res.append(-q[0][0])
        return res

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        for i in range(0,k):
            heapq.heappush(q, (-nums[i], i)) #q = [-val, i]
        arr= [-q[0][0]]
        for i in range(k, len(nums)):
            while q and q[0][1] <= i - k:
                heapq.heappop(q)
            heapq.heappush(q, (-nums[i], i))
            arr.append(-q[0][0])
        return arr