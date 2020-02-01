class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        # low: the lowest index
        # high: the height index
        # profit: prices(high)-prices(low)
        if not prices:
            return 0
        lowVal, profit = prices[0], 0
        for price in prices:
            if price - lowVal > profit:
                profit = price - lowVal
            lowVal = min(lowVal, price)
        return profit
                
             
