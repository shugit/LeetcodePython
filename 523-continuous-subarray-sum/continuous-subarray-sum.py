class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        preSum = [0]
        for n in nums:
            preSum.append(preSum[-1] + n)
        valToIndex = {}
        for i in range(len(preSum)):
            val = preSum[i] % k
            if val not in valToIndex:
                valToIndex[val] = i
        for i in range(1, len(preSum)):
            need = preSum[i] % k
            if need in valToIndex:
                if i - valToIndex[need] >= 2:
                    return True
        return False