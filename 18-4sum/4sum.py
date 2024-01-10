class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:        
        nums.sort()
        return self.kSum(nums,target, 4)

    def sol1(self, nums,target):
        res = set()
        if len(nums) < 4 :
            return res
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                left , right = j+1, len(nums)-1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total > target:
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        l = [nums[i],nums[j],nums[left],nums[right]]
                        res.add(tuple(l))
                        left += 1
        return res

    def kSum(self, nums, target, k):
        res = []
        def twoSum(nums, target):
            res = []
            l, r = 0, len(nums)-1
            while l < r:
                total = nums[l] + nums[r]
                if total < target or (l > 0 and nums[l-1] == nums[l]):
                    l += 1
                elif total > target or (r > len(nums) and nums[r] == nums[r+1]):
                    r -= 1
                else:
                    res.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
            return res

        if not nums:
            return res
        if k == 2:
            return twoSum(nums, target)
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                for subset in self.kSum(nums[i+1:], target-nums[i], k-1):
                    res.append([nums[i]] + subset)
        return res