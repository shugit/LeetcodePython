class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def bt(opened, closed):
            if opened == closed == n:
                res.append("".join(stack))
                return
            if opened < n:
                stack.append("(")
                bt(opened + 1, closed)
                stack.pop()
            if closed < n and opened > closed:
                stack.append(")")
                bt(opened, closed + 1)
                stack.pop()
        bt(0, 0)
        return res