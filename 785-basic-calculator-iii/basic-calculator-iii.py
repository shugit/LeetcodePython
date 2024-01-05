class Solution:
    def calculate(self, s: str) -> int:
        q = deque(s)
        def dfs():
            stack = []
            res = 0
            sign = "+"
            while q:
                node = q.popleft()
                if node.isdigit():
                    res = 10 * res + int(node)
                if node == "(":
                    res = dfs()
                if not node.isdigit() or not q:
                    if sign == "+":
                        stack.append(res)
                    elif sign == '-':
                        stack.append(-res)
                    elif sign == "*":
                        stack[-1] = stack[-1] * res
                    elif sign == '/':
                        stack[-1] = int(stack[-1] / res)
                    res = 0
                    sign = node
                if node == ')':
                    break
            return sum(stack)
        return dfs()