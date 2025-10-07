class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        n = len(prices)
        if k >= n // 2:  # 可以做无限次交易
            return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))

        dp = [[0] * 2 for _ in range(k + 1)]  # dp[j][0/1]

        # 初始化
        for j in range(k + 1):
            dp[j][1] = float('-inf')

        for price in prices:
            for j in range(k, 0, -1):
                dp[j][0] = max(dp[j][0], dp[j][1] + price)
                dp[j][1] = max(dp[j][1], dp[j - 1][0] - price)

        return dp[k][0]
