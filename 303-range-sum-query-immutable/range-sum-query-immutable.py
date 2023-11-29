class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] * len(nums)
        prefix = 0
        for i,n in enumerate(nums):
            prefix += n
            self.prefix_sum[i] = prefix


    def sumRange(self, left: int, right: int) -> int:
        # print(self.prefix_sum)
        return self.prefix_sum[right] - (self.prefix_sum[left-1] if left > 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)