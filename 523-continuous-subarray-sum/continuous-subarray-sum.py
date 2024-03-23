class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        h = {0 : -1}
        curSum = 0
        for i, n in enumerate(nums):
             curSum += n
             r = curSum % k
             if r in h:
                dist = i - h[r]
                if dist > 1:
                    return True
             else:
                h[r] = i
        return False