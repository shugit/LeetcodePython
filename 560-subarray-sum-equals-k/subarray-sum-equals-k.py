class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}
        # prefixSum[0] = 1
        curSum = 0
        res = 0
        for i, n in enumerate(nums):
            curSum += n
            if curSum - k in prefixSum:
                res += prefixSum[curSum-k]
            prefixSum[curSum]  = 1 + prefixSum.get(curSum, 0)
        return res