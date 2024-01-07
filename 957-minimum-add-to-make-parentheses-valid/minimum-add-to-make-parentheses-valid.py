class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        need = 0
        for n in s:
            if n == '(':
                need += 1
            elif n == ')':
                need -= 1
                if need == -1:
                    need = 0
                    res += 1
        return res + need