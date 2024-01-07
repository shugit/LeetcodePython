class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        dp = [0] * (len(s)+1)
        for i, c in enumerate(s):
            if s[i] == "(":
                stack.append(i)
                dp[i+1] = 0
            else:
                if stack:
                    leftIdx = stack.pop()
                    size = i - leftIdx + 1 + dp[leftIdx]
                    dp[i+1] = size
                else:
                    dp[i+1] = 0
        return max(dp)