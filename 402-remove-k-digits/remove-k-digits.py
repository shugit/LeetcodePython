class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while k > 0 and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            if not stack and n == "0":
                continue
            stack.append(n)
        while k > 0 and stack:
            stack.pop()
            k -= 1
        return "".join(stack) if stack else "0"