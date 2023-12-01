class Solution:
    def jump_dp(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [inf] * n
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            if nums[i]+i >= n:
                dp[i] = 1
                continue
            for step in range(1, min(nums[i] + 1, n - i)):
                dp[i] = min(dp[i],  dp[ i + step ] + 1)
        return dp[0]


    def jump(self, nums: List[int]) -> int:
        l,r = 0,0
        res = 0
        while r < len(nums) - 1:
            far = 0
            for i in range(l, r+1):
                far = max(far, i + nums[i])
            l = r + 1
            r = far
            res += 1
        return res
