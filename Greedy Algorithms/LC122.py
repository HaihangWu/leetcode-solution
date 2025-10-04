class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        delta_p = [0 if index == 0 else prices[index] - prices[index - 1] for index, ele in enumerate(prices)]

        profit = 0

        for index, ele in enumerate(delta_p):
            if ele > 0:
                profit += prices[index] - prices[index - 1]

        return profit
