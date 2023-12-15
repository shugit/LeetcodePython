class Solution:
    def maxProfit2(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i,buying) in dp:
                return dp[(i, buying)]
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        return dfs(0, True)

    def maxProfit(self, prices: List[int]) -> int:
        reset, hold, sold = 0, -float('inf'), -float('inf')
        for price in prices:
            prev_sold = sold
            sold = hold + price
            hold = max(hold, reset - price)
            reset = max(reset, prev_sold)
        return max(reset, sold)
            