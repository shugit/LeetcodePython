class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        dp = [0] * (len(s)+1)
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
                dp[i] = 0
            else:
                if stack:
                    leftIdx = stack.pop()
                    size = i - leftIdx + 1 + dp[leftIdx-1]
                    dp[i] = size
                else:
                    dp[i] = 0
        return max(dp)