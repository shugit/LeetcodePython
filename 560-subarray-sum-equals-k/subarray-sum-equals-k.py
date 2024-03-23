class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h = defaultdict(int)
        curSum = 0
        res = 0
        for n in nums:
            curSum += n
            if curSum == k:
                res += 1
            if curSum - k in h:
                res += h[curSum-k]
            h[curSum] += 1
        return res