class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        n = len(prices)
        hold, sold, rest = [0]*n, [0]*n, [0]*n
        hold[0] = -prices[0]

        for i in range(1, n):
            hold[i] = max(hold[i-1], rest[i-1] - prices[i])
            sold[i] = hold[i-1] + prices[i]
            rest[i] = max(rest[i-1], sold[i-1])

        return max(sold[-1], rest[-1])
