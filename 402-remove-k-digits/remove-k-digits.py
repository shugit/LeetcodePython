class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"
        stack = []
        for n in num:
            while stack and stack[-1] > n and k > 0:
                k -= 1
                stack.pop()
            stack.append(n)
        while k > 0:
            k -= 1
            stack.pop()
        i = 0
        while i < len(stack):
            if stack[i] != "0":
                break
            i += 1
        res = "".join(stack[i:])
        return res if len(res) > 0 else "0"