class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.p2(nums)
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        res = [1]*n
        for i in range(1, n):
            prefix[i]  = prefix[i-1] * nums[i-1]
        for i in range(n-2,-1,-1):
            postfix[i] = postfix[i+1] * nums[i+1]
        print(prefix, postfix)
        for i in range(0,n):
            res[i] = prefix[i] * postfix[i]
        return res

    def p2(self, nums):
        n = len(nums)
        res = [1] * n
        for i in range(1,n):
            res[i] = res[i-1] * nums[i-1]
        print(res)
        post = 1
        for i in range(n-2, -1, -1):
            post = post * nums[i+1]
            res[i] = post * res[i]
        return res