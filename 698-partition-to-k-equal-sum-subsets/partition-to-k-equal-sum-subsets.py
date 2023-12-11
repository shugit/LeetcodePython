class Solution:
    def canPartitionKSubsets2   (self, nums: List[int], k: int) -> bool:
        tsum = sum(nums)
        target = tsum // k
        if tsum / k != target:
            return False
        nums.sort(reverse=True)
        used = [False] * len(nums)
        # found = False
        def bt(i, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return bt(0, k-1, 0)
            for j in range(i, len(nums)):
                if i > 0 and not used[i-1] and nums[i] == nums[i-1]:
                    continue
                if used[j] or subsetSum + nums[j] > target:
                    continue
                used[j] = True 
                if bt(j + 1, k, subsetSum + nums[j]):
                    return True
                used[j] = False
            return False
        return bt(0, k, 0)

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k:
            return False

        reqSum = total // k
        subSets = [0] * k
        nums.sort(reverse = True)

        def recurse(i):
            if i == len(nums):    
                return True
            for j in range(k):
                if subSets[j] + nums[i] <= reqSum:
                    subSets[j] += nums[i]
                    if recurse(i + 1):
                        return True
                    subSets[j] -= nums[i]
                    # Important line, otherwise function will give TLE
                    if subSets[j] == 0:
                        break
            return False
        return recurse(0)