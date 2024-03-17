class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        c = 0
        for i in range(len(nums)-1):
            diff = (nums[i+1] - nums[i] - 1)
            if c + diff >= k:
                return nums[i] + (k-c)
            c += diff
        return nums[-1] + (k-c)