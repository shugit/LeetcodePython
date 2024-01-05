class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        ti = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                ti = i - 1
                break
        if ti == -1:
            nums.reverse()
            return
        si = len(nums)-1
        for i in range(len(nums)-1, ti, -1):
            if nums[i] > nums[ti]:
                si = i
                break
        nums[ti], nums[si] = nums[si], nums[ti]
        nums[ti + 1:] = reversed(nums[ti+1:])

        
