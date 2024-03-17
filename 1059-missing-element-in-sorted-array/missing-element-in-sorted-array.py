class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        missed= nums[-1] - nums[0] - (len(nums)-1)
        if missed < k:
            return nums[-1] + k - missed
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] - nums[0] - mid < k:
                l = mid + 1
            else:
                r = mid
        return nums[0] + l + k - 1
            
        