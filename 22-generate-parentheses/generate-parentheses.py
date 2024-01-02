class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # stack = []
        res = []
        def bt(opened, closed, path):
            if opened == closed == n:
                res.append(path)
                return
            if opened < n:
                bt(opened + 1, closed, path + "(")
            if closed < n and opened > closed:
                bt(opened, closed + 1, path +")")
        bt(0, 0, '')
        return res