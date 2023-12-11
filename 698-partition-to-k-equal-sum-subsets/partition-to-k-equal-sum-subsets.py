class Solution:
    def canPartitionKSubsets (self, nums: List[int], k: int) -> bool:
        tsum = sum(nums)
        target = tsum // k
        if tsum / k != target:
            return False
        nums.sort(reverse=True)
        used = set()
        # found = False
        sums = [0]*k
        def bt(i):
            if i == len(nums):
                return True
            for j in range(0, k):
                n = nums[i]
                if n + sums[j] > target:
                    continue
                sums[j] += n
                if bt(i+1):
                    return True
                sums[j] -= n
                if sums[j] == 0:
                    break
            # print(i,k,subsetSum,"False")
            return False
        return bt(0)

    def canPartitionKSubsets2(self, nums: List[int], k: int) -> bool:
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