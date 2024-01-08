class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        dp = [0] * len(s)
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                if stack:
                    leftIdx = stack.pop()
                    size = i - leftIdx + 1 + dp[leftIdx-1]
                    dp[i] = size
        return max(dp)