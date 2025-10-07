class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """

        n = len(prices)
        if n == 0:
            return 0

        hold = -prices[0]
        cash = 0

        for i in range(1, n):
            hold = max(hold, cash - prices[i])
            cash = max(cash, hold + prices[i] - fee)

        return cash
