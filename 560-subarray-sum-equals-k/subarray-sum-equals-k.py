class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefixSum = {0:1}
        # prefixSum[0] = 1
        prefixSum = {}
        curSum = 0
        res = 0
        for n in nums:
            curSum += n
            if curSum == k:
                res += 1
            if curSum - k in prefixSum:
                res += prefixSum[curSum-k]
            prefixSum[curSum]  = 1 + prefixSum.get(curSum, 0)
        return res