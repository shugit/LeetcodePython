class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = {}
        dp_min = {}
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        n = len(nums)
        for i in range(1,n):
            vMax = dp_max[i-1] * nums[i]
            vMin = dp_min[i-1] * nums[i]
            dp_max[i] = max(nums[i], vMax, vMin)
            dp_min[i] = min(nums[i], vMax, vMin)
        return max( max(dp_max.values()),  max(dp_min.values())  )