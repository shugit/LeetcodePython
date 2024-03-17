class Solution:
    def __init__(self, w: List[int]):
        n = len(w)
        self.r = random.Random()
        self.preSum = [0]
        for i in range(len(w)):
            self.preSum.append(self.preSum[-1] + w[i])
        print(self.preSum)

    def pickIndex(self) -> int:
        t = self.r.randint(1, self.preSum[-1])
        print(t)
        def find(nums):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) //2
                if nums[mid] == t:
                    r = mid
                elif nums[mid] < t:
                    l = mid + 1
                else:
                    r = mid
            return l
        return find(self.preSum)-1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()