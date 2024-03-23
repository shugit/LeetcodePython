class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        curSum = 0
        h = {0:-1}
        maxi = 0
        for i, n in enumerate(nums):
            curSum += (-1 if n == 0 else 1)
            if curSum in h:
                maxi = max(maxi, i - h[curSum])
            else:
                h[curSum] = i
        return maxi
