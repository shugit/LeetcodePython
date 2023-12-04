class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        c = Counter()
        left = 0
        for right in range(0, len(nums)):
            c[nums[right]] += 1
            while c[nums[right]] >= 2 and right-left > k:
                c[nums[left]] -= 1
                left += 1
            if c[nums[right]] == 2 and right-left <= k:
                return True
        return False