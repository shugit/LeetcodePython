class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        num = 0
        op = "+"
        stack = []
        for c in s + "+":
            if c.isdigit():
                num = 10 * num + int(c)
            if not c.isdigit() and c != ' ':
                if op == "+":
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == "*":
                    stack[-1] = stack[-1] * num
                elif op == "/":
                    stack[-1] = int(stack[-1]/num)
                op = c
                num = 0
        return sum(stack)