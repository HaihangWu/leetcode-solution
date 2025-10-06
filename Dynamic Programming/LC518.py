class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        size = len(coins)
        mem = [[-1] * (amount + 1) for _ in range(size + 1)]

        def dfs(i, rest):
            # 用前 i 个硬币组成金额 rest 的方法数
            if rest == 0:
                return 1
            if i == 0:
                return 0
            if mem[i][rest] != -1:
                return mem[i][rest]

            res = dfs(i - 1, rest)  # 不用第 i 种硬币
            if rest >= coins[i - 1]:
                res += dfs(i, rest - coins[i - 1])  # 至少用一个第 i 种硬币

            mem[i][rest] = res
            return res

        return dfs(size, amount)
