class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.hashTable(nums)
    def hashTable(self, nums):
        nums.sort()
        res = []
        for i, n1 in enumerate(nums):
            if i >= 1 and nums[i-1] == nums[i]:
                continue
            h = set()
            j = i+1
            while j < len(nums):
                n2 = nums[j]
                if -(n1+n2) in h:
                    res.append([n1, n2, -(n1+n2)])
                    while j + 1 < len(nums) and nums[j] == nums[j+1]:
                        j += 1
                h.add(n2)
                j += 1
        return res

    def twoPointer(self, nums):
        res = set()
        if len(nums) < 3 :
            return res
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) -1
            sum = 0 - nums[i]
            while j < k:
                if nums[j] + nums[k] > sum:
                    k -= 1
                elif nums[j] + nums[k] < sum:
                    j += 1
                else:
                    res.add(tuple([nums[i],nums[j],nums[k]]))
                    j += 1
        return res

