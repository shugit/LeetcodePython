class Solution:
    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
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

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = defaultdict(list)
        for i in range(len(nums)):
            h[nums[i]].append(i)
            if len(h[nums[i]]) >= 2:
                if h[nums[i]][-1] - h[nums[i]][-2] <= k:
                    return True
        return False