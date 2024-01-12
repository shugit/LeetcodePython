class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.downTop(nums)
        # return self.topDown(nums)

    def topDown(self, nums: List[int]) -> int:
        if not nums:
            return 0
        memo = {}
        def dp(i):
            if i == -1:
                return 0
            pre = dp(i-1)
            cur = max(pre + nums[i], nums[i])
            memo[i] = cur
            return cur
        dp(len(nums)-1)
        return max(memo.values())

    def downTop(self, nums):
        n = len(nums)
        dp = {}
        pre = nums[0]
        maxi = nums[0]
        for i in range(1, n):
            pre = max(pre+nums[i], nums[i])
            maxi = max(maxi, pre)
        return maxi

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