class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s // 2
        dp = [False for _ in range(target+1)] 
        dp[0] = True
        # if nums[0] <= target:
        #     dp[nums[0]] = True

        for i in range(1, len(nums)):
            curr = nums[i-1]
            for j in range(target, -1,-1):
                if curr <= j :
                    dp[j] = dp[j] or dp[j-curr]
                    # print(i,j,dp)
            # print(curr,dp)
            if dp[target] == True:
                # print(i,j)
                return True
        return dp[target]