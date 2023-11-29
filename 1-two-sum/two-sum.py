class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        res = []
        for i, n in enumerate(nums):
            if target - n in h:
                return [i, h[target-n]]
            if n not in h:
                h[n] = i
        return []
        