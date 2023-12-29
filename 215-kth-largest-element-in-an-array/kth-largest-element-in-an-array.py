import heapq
class Solution:
    def tooSlow(self, nums,k):
        for i in range(0, k):
            max_i = i
            for j in range(i+1, len(nums)):
                if nums[j] > nums[max_i]:
                    max_i = j
                
            if i != max_i:
                nums[i], nums[max_i] = nums[max_i], nums[i]
            
        # print(nums)
        return nums[k-1]
            
    def findKthLargest3(self, nums: List[int], k: int) -> int:
        arr = [-x for x in nums]
        heapq.heapify(arr)
        for _ in range(k-1):
            heapq.heappop(arr)
        return -heapq.heappop(arr)
        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]