class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2
        dp = [ [False for _ in range(target+1)] for _ in range(len(nums))]
        if nums[0] <= target:
            dp[0][nums[0]] = True

        for i in range(len(nums)):
            for j in range(target+1):
                dp[i][j] = dp[i-1][j]
                if nums[i] == j:
                    dp[i][j] = True
                    continue
                if nums[i] < j :
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
            if dp[i][target] == True:
                return True
        return dp[len(nums)-1][target]