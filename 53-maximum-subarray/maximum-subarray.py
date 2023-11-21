class Solution:
    def maxSubArray_dp(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        print(dp)
        return max(dp.values())

    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float("-inf")
        res = 0
        for num in nums:
            if res > 0:
                res += num
            else:
                res = num
            maxi = max(maxi, res)
        return maxi