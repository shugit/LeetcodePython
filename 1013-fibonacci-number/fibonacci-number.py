class Solution:
    def fib(self, n: int) -> int:
        return self.sol3(n)
    def sol3(self, n):
        if n == 1: 
            return 1
        elif n == 0:
            return 0
        d1, d2 = 1, 0
        for i in range(2, n+1):
            n = d1 + d2
            d2 = d1
            d1 = n
        return d1



    def sol2(self, n):
        memo = {0:0, 1:1}
        def dp(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = dp(n-1) + dp(n-2)
            return memo[n]
        return dp(n)

    def sol1(self, n):
        dic = {}
        dic[1] = 1
        dic[0] = 0
        # print(dic)
        for i in range(2, n+1):
            dic[i] = dic[i-2] + dic[i-1]
        return dic[n]