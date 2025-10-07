class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0

        # 初始化
        dp0 = 0
        dp1 = -prices[0]
        dp2 = 0
        dp3 = -prices[0]
        dp4 = 0

        for p in prices[1:]:
            dp1 = max(dp1, dp0 - p)  # 第一次买入
            dp2 = max(dp2, dp1 + p)  # 第一次卖出
            dp3 = max(dp3, dp2 - p)  # 第二次买入
            dp4 = max(dp4, dp3 + p)  # 第二次卖出

        return dp4
