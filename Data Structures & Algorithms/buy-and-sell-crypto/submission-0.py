class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for i, price in enumerate(prices):
            profit = price - buy
            if buy > price:
                buy = price
            if profit > max_profit:
                max_profit = profit
        return max_profit