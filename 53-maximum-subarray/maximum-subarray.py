class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.topDown(nums)
    def topDown(self, nums: List[int]) -> int:
        if not nums:
            return 0
        memo = {}
        def dp(i):
            if i == -1:
                return 0
            pre = dp(i-1)
            memo[i] = max(pre + nums[i], nums[i])
            return memo[i]
        dp(len(nums)-1)
        return max(memo.values())



    def downtop(self, nums):
        n = len(nums)
        dp = {}
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp.values())

    def slindingwindow(self, nums: List[int]) -> int:
        maxi = float("-inf")
        res = 0
        for num in nums:
            if res > 0:
                res += num
            else:
                res = num
            maxi = max(maxi, res)
        return maxi