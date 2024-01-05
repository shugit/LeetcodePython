class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                n = stack.pop()
                stack[-1] += max(2 * n, 1)
        return stack.pop()