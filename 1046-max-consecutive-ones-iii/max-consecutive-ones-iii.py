class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxi = 0
        left = 0
        flipped = 0
        for right in range(0, len(nums)):
            if nums[right] == 0:
                flipped += 1
            while flipped > k:
                flipped -= (1-nums[left])
                left += 1
            maxi = max(maxi, right - left + 1)
        return maxi
        # return right - left + 1

