class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        opened, closed = 0,0
        def bt():
            nonlocal opened, closed
            if opened == closed == n:
                res.append("".join(stack))
                return
            if opened < n:
                stack.append("(")
                opened += 1
                bt()
                opened -= 1
                stack.pop()
            if closed < n and opened > closed:
                stack.append(")")
                closed += 1
                bt()
                closed -= 1
                stack.pop()
        bt()
        return res