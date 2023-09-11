class Solution:
    def numDecodings(self, s: str) -> int:
        # return self.numDecodings2(s)
        size = len(s)
        dp = [0 for _ in range(size + 1)]
        dp[0] = 1
        for i in range(1, size + 1):
            cur = s[i-1]
            prev = s[i-2]
            comb  = prev + cur
            # if cur != '0':
            #     dp[i] += dp[i-1]
            # if i > 1 and prev != '0' and int(prev+cur) <= 26:
            #     dp[i] += dp[i-2]
            #只能判断哪种状态是可以加入方案的，不能用排除法
            if cur != '0':
                dp[i] += dp[i-1]
            if i>1 and prev !='0' and int(comb) <=26:
                dp[i] += dp[i-2]
        return dp[size]

# class Solution:
    def numDecodings2(self, s: str) -> int:
        size = len(s)
        dp = [0 for _ in range(size + 1)]
        dp[0] = 1
        for i in range(1, size + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[size]