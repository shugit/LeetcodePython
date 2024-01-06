class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return self.sol2(temperatures)

    def sol2(self, temperatures):
        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            t = temperatures[i]
            while stack and temperatures[stack[-1]] <= t:
                stack.pop()
            res[i] =  stack[-1]-i if stack else 0
            stack.append(i)
        return res


    def sol1(self, temperatures):
        stack = []
        res = [0 for _ in temperatures]
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                prev_i = stack.pop()
                res[prev_i] = (i - prev_i)
            stack.append(i)
        return res