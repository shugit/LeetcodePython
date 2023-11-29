class Solution:
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        h = {}
        res = []
        for i, n in enumerate(nums):
            if target - n in h:
                return [i, h[target-n]]
            if n not in h:
                h[n] = i
        return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i , n in enumerate(nums):
            h[n] = i
        for i, n in enumerate(nums):
            if target - n in h and i != h[target-n]:
                return [i, h[target-n]]
        return []
            
        