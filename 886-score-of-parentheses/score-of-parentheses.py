class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                n = stack.pop()
                if n == 0 :
                    stack[-1] += 1
                else:
                    stack[-1] += 2 * n
        return stack.pop()