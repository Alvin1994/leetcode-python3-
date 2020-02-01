class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        # curtPrice: current price
        # prePrice: previous price
        # low: index of lower price
        if not prices:
            return 0
        low, profit, rst = prices[0], 0, 0
        for i in range(len(prices)-1):
            if prices[i+1] - prices[i] < 0:
                low = prices[i+1]
                rst += profit
                profit = 0
            else:
                profit = prices[i+1] - low
        rst += profit
        return rst
        