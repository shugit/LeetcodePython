class Solution:
    def canJump2(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[len(nums)-1] = True
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= len(nums):
                dp[i] = True
            else:
                for step in range(1, nums[i]+1):
                    if dp[i + step] == True:
                        dp[i] = True
                        break
        return dp[0]

    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal==0
