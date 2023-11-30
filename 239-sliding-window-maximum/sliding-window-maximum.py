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
        q = deque()
        res = []
        for i in range(0,k):
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
        res.append(q[0])
        for i in range(k, len(nums)):
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
            if q[0] == nums[i-k]:
                q.popleft()
            res.append(q[0])
        return res
            