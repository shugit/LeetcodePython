class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums)
        while l < r:
            mid = (l + (r-l)//2) //2 * 2
            if mid+1 >= len(nums):
                return nums[mid]
            if nums[mid] == nums[mid+1]:
                l = mid + 2
            else:
                r = mid
        return nums[l]