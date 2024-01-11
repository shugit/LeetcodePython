class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.sol2(nums)

    def sol3(self, nums):
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def sol1(self, nums):
        dp = []
        for num in nums:
            i = bisect_left(dp, num)
            if i == len(dp):
                dp.append(num)
            else:
                dp[i] = num
        return len(dp)

    def sol2(self, nums: List[int]) -> int:
        memo = {0:1}
        def dp(nums, n):
            if n in memo:
                return memo[n]
            res = 1
            for i in range(n-1,-1,-1):
                if nums[i] < nums[n]:
                    res = max(res, dp(nums, i) + 1)
            memo[n] = res
            # print(memo)
            return memo[n]
        for n in range(len(nums)-1, -1,-1):
            dp(nums, n)
        return max(memo.values())