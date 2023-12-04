class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxi = 0
        left = 0
        flipped = 0
        for right in range(0, len(nums)):
            flipped += (1-nums[right])
            while flipped > k:
                flipped -= (1-nums[left])
                left += 1
            maxi = max(maxi, right - left + 1)
        return maxi

