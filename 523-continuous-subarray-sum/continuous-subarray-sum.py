class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        h = {0 : -1}
        preSum = [0]
        for n in nums:
            preSum.append(preSum[-1] + n)
        for i, n in enumerate(nums):
             r = preSum[i+1] % k
             if r in h:
                dist = i - h[r]
                if dist > 1:
                    return True
             else:
                h[r] = i
        return False