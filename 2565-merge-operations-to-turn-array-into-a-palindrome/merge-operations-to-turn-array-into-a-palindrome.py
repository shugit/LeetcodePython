class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] == nums[r]:
                l += 1
                r -= 1
            else:
                if nums[l] + nums[l+1] < nums[r] + nums[r-1]:
                    nums[l+1] += nums[l]
                    l += 1
                else:
                    nums[r-1] += nums[r]
                    r -= 1
                res += 1
        return res