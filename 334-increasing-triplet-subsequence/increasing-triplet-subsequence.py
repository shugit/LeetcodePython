class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = min2 = float("inf")
        i = 0
        for n in nums:
            if min1 < min2 < n:
                return True
            elif n < min1:
                min1 = n
                # print(min1,m
            elif min1 < n < min2:
                min2 = n
                # print(min2)
        return False