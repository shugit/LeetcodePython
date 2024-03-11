class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right -left)  //2
            if mid == 0 and nums[mid+1] < nums[mid]: #leftmost element
                return mid
            elif mid == len(nums) - 1 and nums[mid-1] < nums[mid]: #rightmost element
                return mid
            elif nums[mid-1] < nums[mid] and nums[mid+1] < nums[mid]: # mid is peak
                return mid
            elif nums[mid + 1] > nums[mid]: # mid < right
                left = mid + 1
            else: # mid < left
                right = mid - 1
        # return left
            