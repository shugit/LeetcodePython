class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = [x for x in prices]
        stack = []
        for i in range(len(prices)-1, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            res[i] = res[i] - stack[-1] if stack else res[i]
            stack.append(prices[i])
        return res