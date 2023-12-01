class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [inf] * n
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            if nums[i]+i >= n:
                dp[i] = 1
                continue
            for step in range(1, nums[i] + 1):
                if i + step <= n:
                    dp[i] = min(dp[i],  dp[ i + step ] + 1)
        return dp[0]


    def jump_greedy(self, nums: List[int]) -> int:
        return 0
