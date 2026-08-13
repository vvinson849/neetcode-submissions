class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]
        sell = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                sell = prices[i]
            if prices[i] > sell:
                sell = prices[i]
                maxProfit = max(sell-buy, maxProfit)
        return maxProfit
