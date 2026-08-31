class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0
        for sell in range(1, len(prices)):
            if prices[sell] - prices[buy] < 0:
                buy = sell
            max_profit = max(max_profit, prices[sell] - prices[buy])

        return max_profit

        