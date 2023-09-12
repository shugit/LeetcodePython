class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        h = {}
        for n in nums:
            if n in h:
                h[n] += 1
            else:
                h[n] = 1
        for k,v in h.items():
            if v != 2:
                return k
        