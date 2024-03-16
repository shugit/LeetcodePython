class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if d.get(num):
                d[num] += 1
            else:
                d[num] = 1
        
        sort_array = sorted(d.items(), key=lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(sort_array[i][0])
        return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        if k == len(nums):
            return nums
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get) 