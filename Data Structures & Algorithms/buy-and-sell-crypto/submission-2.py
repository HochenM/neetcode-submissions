class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        y,t= 0,1
        maxP = 0

        while t <len(prices):
            if prices[y] < prices[t]:
                profit = prices[t] - prices[y]
                maxP = max(maxP,profit)
            else:
                y=t
            t +=1
        return maxP
        