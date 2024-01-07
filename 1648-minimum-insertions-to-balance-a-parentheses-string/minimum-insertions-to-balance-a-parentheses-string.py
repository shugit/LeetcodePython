class Solution:
    def minInsertions(self, s: str) -> int:
        left, need = 0, 0
        for n in s:
            if n == "(":
                need += 2
                if need % 2 == 1:
                    left += 1
                    need -= 1
            else:
                need -= 1
                if need == -1:
                    left += 1
                    need = 1
        return left + need 