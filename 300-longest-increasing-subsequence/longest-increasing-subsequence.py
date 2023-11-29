class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(n,-1,-1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        # print(dp)
        return max(dp)  

    def lengthOfLIS2(self, nums: List[int]) -> int:
        return 0
