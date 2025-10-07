class Solution(object):
    def maxProfit(self, prices):
        size = len(prices)
        mem = [-1] * size

        def dfs(i, min_price):
            if i == 0:
                return 0, prices[0]

            profit_prev, min_prev = dfs(i - 1, min_price)

            profit_today = max(profit_prev, prices[i] - min_prev)
            min_today = min(min_prev, prices[i])

            mem[i] = profit_today
            return profit_today, min_today

        result, _ = dfs(size - 1, prices[0])
        return result
