class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        currentProfit = 0
        maxProfit = 0
        buy = prices[0]
        for i in range(0,n):
            if buy>prices[i]:
                buy = prices[i]
            
            currentProfit = prices[i] - buy
            maxProfit = max(currentProfit,maxProfit)

        return maxProfit