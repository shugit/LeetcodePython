class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        pairs = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c in pairs:
                stack.append(c)
            elif len(stack) == 0 or c != pairs[stack.pop()] :
                return False
        return len(stack) == 0
                