class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        count = [1] * len(nums)
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
                    
        # print(dp, count)
        maxi = max(dp) 
        cnt = 0
        for i,n in enumerate(dp):
            if n == maxi:
                cnt += count[i]
        return cnt