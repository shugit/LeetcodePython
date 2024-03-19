class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        h = defaultdict(list)
        for i in range(len(nums) -1, -1, -1):
            for j in range(len(nums[i])):
                h[i+j].append(nums[i][j])
        res = []
        for k, v in sorted(h.items()):
            res += v
        return res