class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)-1
        print(n)
        dp = {}
        dp[-1] = 0
        dp[0] = nums[0]
        nums.append(0)
        i = 1
        while i <= n:
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            i += 1
        return dp[n]