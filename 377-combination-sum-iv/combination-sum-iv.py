class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # return self.combinationSum5(nums,target)
        size = len(nums)
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for j in range(target+1):
            for i in range(1,size + 1):
                cur = nums[i-1]
                if j-cur >=0:
                    dp[j] += dp[j-cur]
        return dp[target]

    def combinationSum5(self, nums: List[int], target: int) -> int:
        size = len(nums)
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1

        for w in range(target + 1):
            for i in range(1, size + 1):
                if w >= nums[i - 1]:
                    dp[w] = dp[w] + dp[w - nums[i - 1]]
            print(dp)
            
        return dp[target]